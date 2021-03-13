const problems = require('./problems.json');
const metaDataById = require('./metadata.json');
const fetchMetadata = require('./fetchMetadata');
const fs = require('fs');
const path = require('path');

const promises = [];

problems.forEach((problem) => {
  const id = problem.questionId;
  if (metaDataById[id] == null && id <= 200 && problem.isPaidOnly === false && problem.categoryTitle === 'Algorithms' && id < 1000000) {
    promises.push(Promise.resolve(
      fetchMetadata(problem.titleSlug).then((data) => {
        try {
          // console.log('!!!!!!');
          // console.log(data);
          data = JSON.parse(data);
          // console.log('######');
          // console.log(data);
          let metaData = data.data.question.metaData;
          metaData = JSON.parse(metaData);
          metaData.exampleTestcases = data.data.question.exampleTestcases;
          metaDataById[id] = metaData;
        } catch (e) {
          console.error(e);
        }
      }).catch((err) => console.error(err))
    ));
  }
});

async function main() {
  console.log(promises.length);
  await Promise.all(promises);
  // console.log(metaDataById);
  // for (const id in moreTestcases) {
  //   metaDataById[id].exampleTestcases += '\n' + moreTestcases[id].exampleTestcases;
  //   // metaDataById[id].exampleResult += '\n' + moreTestcases[id].exampleResult;
  // }
  fs.writeFileSync(path.join(__dirname, './metadata.json'), JSON.stringify(metaDataById, undefined, '  '));
}

main();
