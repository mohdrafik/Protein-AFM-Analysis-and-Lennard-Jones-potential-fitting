using System;
class Program
{
    static void ModifyValue(ref int number)
    {
        // Modify the value of 'number' through the reference
        number = 20;
    }

    static void Main()
    {
        int value = 10;

        Console.WriteLine("Original value: " + value);

        // Pass 'value' by reference to the method
        ModifyValue(ref value);

        Console.WriteLine("Modified value: " + value);
    }
}
