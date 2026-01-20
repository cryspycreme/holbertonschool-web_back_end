export default function createInt8TypedArray(length, position, value) {
  // create Int8Array of the given lengrth
  const typedArray = new Int8Array(length);

  // check if position is valid
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  // set the value at the given position
  typedArray[position] = value;

  // return the underlying ArrayBuffer
  return typedArray.buffer;
}
