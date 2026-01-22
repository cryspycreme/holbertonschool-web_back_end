export default function handleResponseFromAPI(promise) {
  promise
    .then((result) => {
      console.log('Got a response from the API');
      return {
        status: 200,
        body: 'success',
      };
    })
    .catch((errorMessage) => {
      console.log('Error thrown');
      return new Error();
    });
}
