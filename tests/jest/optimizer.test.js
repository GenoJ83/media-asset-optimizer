const { calculateDimensions, calculateSavings } = require('../../js/optimizer');

describe('Media Optimizer Math', () => {
  it('calculates proportional height on width clamp', () => {
    const dims = calculateDimensions(2000, 1000, 1000);
    expect(dims.width).toBe(1000);
    expect(dims.height).toBe(500);
  });
  it('calculates savings percentage', () => {
    expect(calculateSavings(1000, 400)).toBe(60.0);
  });
});
