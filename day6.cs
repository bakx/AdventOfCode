using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            const int gridSize = 1000;

            // Initiate the grid
            int[,] grid = new int[gridSize + 1, gridSize + 1];

            for (int x = 0; x <= gridSize; x++)
                for (int y = 0; y <= gridSize; y++)
                    grid[x, y] = 0;

            // Keep track of the lights turned on
            int lightsOn = 0;

            // Read the file
            string line = string.Empty;

            StreamReader reader = new StreamReader("./input/day6.txt");
            while (!reader.EndOfStream)
                HandleInstruction(ref grid, reader.ReadLine());

            // check grid
            for (int x = 0; x <= gridSize; x++)
                for (int y = 0; y <= gridSize; y++)
                    if (grid[x, y] == 1)
                        lightsOn++;

            Console.WriteLine(lightsOn.ToString() + " lights turned on");
            Console.ReadKey();
        }

        static void HandleInstruction(ref int[,] grid, string instruction)
        {
            int[,] _range_x = new int[2, 2];
            int[,] _range_y = new int[2, 2];

            string[] _ranges = instruction
                .Replace("turn off ", "")
                .Replace("turn on ", "")
                .Replace("toggle ", "")
                .Replace("through ", "")
                .Split(' ');

            _range_x[0, 0] = int.Parse((_ranges[0].Split(',')[0]));
            _range_x[0, 1] = int.Parse((_ranges[1].Split(',')[0]));
            _range_y[0, 0] = int.Parse((_ranges[0].Split(',')[1]));
            _range_y[0, 1] = int.Parse((_ranges[1].Split(',')[1]));

            // At this point, we know the ranges.
            for (int x = _range_x[0,0]; x <= _range_x[0,1]; x++)
            {
                for (int y = _range_y[0, 0]; y <= _range_y[0, 1]; y++)
                {
                    if (instruction.StartsWith("turn off"))
                        grid[x, y] = 0;
                    else if (instruction.StartsWith("turn on"))
                        grid[x, y] = 1;
                    else
                        grid[x, y] = (grid[x, y] == 0) ? 1 : 0;
                }
            }
        }
    }
}

