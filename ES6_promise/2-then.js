export default function handleResponseFromAPI(promise) {
  const myPromise = new Promise((resolve, reject) => {
    if (promise) {
      resolve({
        status: 200,
        body: 'Success',
      });
    } else {
      reject(new Error());
    }
  });
  // ..then what happens after a resolve?
  myPromise
    .then((result) => {
      console.log('Got a response from the API');
    })
    .catch((errorMessage) => {
      console.log('Error thrown');
    });
}
