const problems = require('./problems.json');
const metaDataById = require('../dist/metadata.json');
const fetchMetadata = require('./fetchMetadata');
const fs = require('fs');
const path = require('path');

const promises = [];

problems.forEach((problem) => {
  const id = problem.questionId;
  if (id > 100 && id <= 200 && problem.isPaidOnly === false && problem.categoryTitle === 'Algorithms' && id < 1000000) {
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
        } catch (e) { }
      })
    ));
  }
});

async function main() {
  await Promise.all(promises);
  // console.log(metaDataById);
  fs.writeFileSync(path.join(__dirname, '../dist/metadata.json'), JSON.stringify(metaDataById, undefined, '  '));
}

main();
