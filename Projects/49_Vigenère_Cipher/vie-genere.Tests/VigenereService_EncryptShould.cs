using vie_genere.Parameters;

namespace vie_genere.Tests;
public class VigenereService_EncryptShould
{
    [Theory]
    [InlineData("C", "B", "AB")]
    [InlineData("A", "C", "AB")]
    public void Encrypt_InputOrKeyNotInAlphabet_ThrowArgumentOutOfRangeException(string input, string key, string alphabet)
    {
        // Arrange
        var maxDegreeOfParallelism = 10;
        var cancellationToken = new CancellationTokenSource().Token;
        var vigenereData = new VigenereData(new EncryptParameters
        {
            Alphabet = alphabet,
            Input = "A",
            Key = "B",
            MaxDegreeOfParallelism = maxDegreeOfParallelism
        })
        {
            Input = input,
            Key = key.ToCharArray()
        };

        // Act
        // Assert
        Assert.Throws<AggregateException>(() => VigenereService.Encrypt(vigenereData, cancellationToken, maxDegreeOfParallelism));
    }

    [Fact]
    public void Encrypt_ValidInput_ReturnOutputOfSameLength()
    {
        // Arrange
        var vigenereData = new VigenereData(new EncryptParameters
            {
                Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                Input = "THIS IS A TEST SENTENCE",
                Key = "KEY",
                MaxDegreeOfParallelism = 10
            });
        var expected = "DLGC MQ K XCCX QORRORAO";

        // Act
        var result = VigenereService.Encrypt(vigenereData,
            new CancellationTokenSource().Token);

        // Assert
        Assert.NotEqual(vigenereData.Input, result);
        Assert.Equal(vigenereData.Input.Length, result.Length);
        Assert.Equal(expected, result);
    }
}
