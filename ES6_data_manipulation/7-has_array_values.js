export default function hasValuesFromArray(set, array) {
  if (array.every((value) => set.has(value))) {
    return true;
  } else return false;
}
