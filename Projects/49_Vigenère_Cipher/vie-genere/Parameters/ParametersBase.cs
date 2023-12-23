using CommandLine;

namespace vie_genere.Parameters;
public abstract class ParametersBase
{
    [Option('i', "input", HelpText = "Input to decrypt or encrypt.", Required = true)]
    public required string Input {get;set;}

    [Option('t', "threads", HelpText = "Maximum amout of threads.", Default = 10, Required = false)]
    public required int MaxDegreeOfParallelism {get;set;}

    [Option('a', "alphabet", HelpText = "Set of letters used for the plain text and the encrypted.", Required = false, Default = "ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
    public required string Alphabet {get;set;}

    [Option('k', "key", HelpText = "Key to use to encrypt", Required = true)]
    public required string Key {get;set;}
}
