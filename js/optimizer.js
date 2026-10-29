function calculateDimensions(width, height, maxWidth) {
  if (width <= maxWidth) return { width, height };
  const ratio = maxWidth / width;
  return { width: maxWidth, height: Math.round(height * ratio) };
}
function calculateSavings(originalBytes, optimizedBytes) {
  if (!originalBytes) return 0;
  return Number((((originalBytes - optimizedBytes) / originalBytes) * 100).toFixed(2));
}
module.exports = { calculateDimensions, calculateSavings };
