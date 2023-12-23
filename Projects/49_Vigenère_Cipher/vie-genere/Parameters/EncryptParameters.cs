using CommandLine;

namespace vie_genere.Parameters;

[Verb("encrypt", isDefault: true, aliases: new string[]{ "e", "enc" }, HelpText = "Encrypt the input data using alphabet.")]
public class EncryptParameters : ParametersBase
{
    
}
