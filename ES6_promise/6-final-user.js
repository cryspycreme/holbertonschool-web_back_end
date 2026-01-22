import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const promiseA = signUpUser();
  const promiseB = uploadPhoto();

  const promises = [promiseA, promiseB];

  return Promise.allSettled(promises).then(([user, photoResponse]) => {
    [
      {
        status: 'fulfilled',
        value: user,
      },
      {
        status: 'fulfilled',
        value: photoResponse,
      },
    ];
  });
}
