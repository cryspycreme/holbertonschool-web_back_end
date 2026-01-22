import { uploadPhoto } from './utils';
import { createUser } from './utils';

export default function handleProfileSignup() {
  const promiseA = uploadPhoto();
  const promiseB = createUser();

  const promises = [promiseA, promiseB];

  Promise.all(promises)
    .then(([photoResponse, user]) => {
      const photo = photoResponse.body;
      const firstName = user.firstName;
      const lastName = user.lastName;
      console.log(photo + ' ' + firstName + ' ' + lastName);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
