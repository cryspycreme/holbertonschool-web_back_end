export default function getResponseFromAPI() {
  const myPromise = new Promise((resolve, reject) => {
    const success = true;
    if (success) {
      resolve('Success');
    } else {
      reject();
    }
  });
  return myPromise;
}
