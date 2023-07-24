// See https://aka.ms/new-console-template for more information
//Console.WriteLine("Hello, World!");

try
{
    Console.WriteLine("Enter your age");
    string Age = Console.ReadLine();
    int _age = int.Parse(Age);
    Console.WriteLine($"My age is {Age}");

}
catch{
    Console.WriteLine("Inavlid input");
}
