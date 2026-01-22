export default function handleResponseFromAPI(promise) {
  promise
    .then((result) => {
      console.log('Got a response from the API');
    })
    .catch((errorMessage) => {
      console.log('Error thrown');
    });
}
