namespace vie_genere.Tests;

public class VigenereService_PositiveModShould
{
    [Theory]
    [InlineData(-10, 9)]
    [InlineData(-1, 9)]
    public void PositiveMod_LessThanZero_ReturnPositiveIntLowerThanModulo(int val, int modulo)
    {
        // Arrange
        // Act
        var result = VigenereService.PositiveMod(val, modulo);

        // Assert
        Assert.True(result < modulo && result >= 0);
    }

    [Theory]
    [InlineData(9, 9)]
    [InlineData(10, 9)]
    [InlineData(100, 9)]
    public void PositiveMod_GreaterOrEqualThanModulo_ReturnPositiveIntLowerThanModulo(int val, int modulo)
    {
        // Arrange
        // Act
        var result = VigenereService.PositiveMod(val, modulo);

        // Assert
        Assert.True(result < modulo && result >= 0);
    }

    [Theory]
    [InlineData(0)]
    [InlineData(-1)]
    public void PositiveMod_NegativeModulo_ThrowsArgumentOutOfRangeException(int modulo)
    {
        // Arrange
        var random = new Random();
        var notImportantVal = random.Next();

        // Act
        // Assert
        Assert.Throws<ArgumentOutOfRangeException>(() => VigenereService.PositiveMod(notImportantVal, modulo));
    }
}