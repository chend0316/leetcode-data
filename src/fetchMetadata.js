var request = require('request');

module.exports = function (titleSlug) {
  return new Promise((resolve, reject) => {
    var options = {
      'method': 'GET',
      'url': 'https://leetcode-cn.com/graphql/',
      'headers': {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        query: `query questionData($titleSlug: String!) {
    question(titleSlug: $titleSlug) {
    metaData
    exampleTestcases
    __typename
  }
}`,
        variables: { "titleSlug": titleSlug }
      })
    };
    request(options, function (error, response) {
      if (error) {
        reject(error);
      } else {
        resolve(response.body);
      }
    });
  });
};
