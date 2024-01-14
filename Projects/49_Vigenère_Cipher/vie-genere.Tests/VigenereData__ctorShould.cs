using vie_genere.Parameters;

namespace vie_genere.Tests;
public class VigenereData__ctorShould
{
    [Fact]
    public void Ctor_ValidParameters_ReturnFulfillFields()
    {
        // Arrange
        var parametersBase = new EncryptParameters{
            Input = "TEST",
            Key = "KEY",
            Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            MaxDegreeOfParallelism = 10
        };

        // Act
        var vigenereData = new VigenereData(parametersBase);

        // Assert
        Assert.Equal(parametersBase.Input, vigenereData.Input);
        Assert.Equal(parametersBase.Key.ToCharArray(), vigenereData.Key);
        Assert.Equal(parametersBase.Alphabet.ToCharArray(), vigenereData.Alphabet);
    }

    [Theory]
    [MemberData(nameof(GetInvalidEmptyEncryptParameters), MemberType = typeof(VigenereData__ctorShould))]
    public void Ctor_OneOfParamIsEmpty_ThrowArgumentNullException(EncryptParameters encryptParameters)
    {
        // Arrange
        // Act
        // Assert
        Assert.Throws<ArgumentNullException>(() => new VigenereData(encryptParameters));
    }

    [Fact]
    public void Ctor_AlphabetHasSameLetterTwice_ThrowArgumentException()
    {
        // Arrange
        var parametersBase = new EncryptParameters{
            Input = "A",
            Key = "A",
            Alphabet = "ABB",
            MaxDegreeOfParallelism = 10
        };

        // Act
        // Assert
        Assert.Throws<ArgumentException>(() => new VigenereData(parametersBase));
    }

    [Fact]
    public void Ctor_InputHasLetterNotInAlphabet_ThrowArgumentOutOfRangeException()
    {
        // Arrange
        var parametersBase = new EncryptParameters{
            Input = "AB",
            Key = "A",
            Alphabet = "A",
            MaxDegreeOfParallelism = 10
        };

        // Act
        // Assert
        Assert.Throws<ArgumentOutOfRangeException>(() => new VigenereData(parametersBase));
    }

    [Fact]
    public void Ctor_KeyHasLetterNotInAlphabet_ThrowArgumentOutOfRangeException()
    {
        // Arrange
        var parametersBase = new EncryptParameters{
            Input = "A",
            Key = "AB",
            Alphabet = "A",
            MaxDegreeOfParallelism = 10
        };

        // Act
        // Assert
        Assert.Throws<ArgumentOutOfRangeException>(() => new VigenereData(parametersBase));
    }

    public static IEnumerable<object[]> GetInvalidEmptyEncryptParameters()
    {
        yield return new object[]
        {
            new EncryptParameters{
                Input = "",
                Key = "KEY",
                Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                MaxDegreeOfParallelism = 10
            }
        };
        yield return new object[]
        {
            new EncryptParameters{
                Input = "TEST",
                Key = "",
                Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                MaxDegreeOfParallelism = 10
            }
        };
        yield return new object[]
        {
            new EncryptParameters{
                Input = "TEST",
                Key = "KEY",
                Alphabet = "",
                MaxDegreeOfParallelism = 10
            }
        };
    }
}
