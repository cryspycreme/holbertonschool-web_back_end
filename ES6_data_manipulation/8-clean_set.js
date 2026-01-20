export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string') {
    return '';
  }

  // convert set to array, and use filter+map
  const filtered = [...set]
    .filter((value) => value.startsWith(startString))
    .map((value) => value.slice(startString.length));

  // join with "-"
  return filtered.join('-');
}
