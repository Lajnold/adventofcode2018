using System;
using System.Collections.Generic;

namespace day11cs
{
    class Program
    {
        public static int GetSerial()
        {
            return 8141;
        }

        static int GetCellPower(int x, int y)
        {
            int rackId = x + 10;
            int power = rackId * y;
            power += GetSerial();
            power *= rackId;
            power = power / 100 % 10;
            power -= 5;
            return power;
        }

        static int GetSquarePower(int x, int y, int size)
        {
            int power = 0;
            for (int xi = 0; xi < size; xi++)
            {
                for (int yi = 0; yi < size; yi++)
                {
                    power += GetCellPower(x + xi, y + yi);
                }
            }
            return power;
        }

        static int GetSquarePowerWithMemoization(int x, int y, int size, Dictionary<Tuple<int, int>, int> cache)
        {
            if (size == 1)
            {
                var power = GetCellPower(x, y);
                cache[Tuple.Create(x, y)] = power;
                return power;
            }
            else
            {
                int power = cache[Tuple.Create(x, y)];
                for (int i = 0; i < size; i++)
                {
                    power += GetCellPower(x + size - 1, y + i);
                    power += GetCellPower(x + i, y + size - 1);
                }

                cache[Tuple.Create(x, y)] = power;
                return power;
            }

        }

        static void Part1()
        {
            int maxPower = int.MinValue;
            int maxPowerX = -1;
            int maxPowerY = -1;
            for (int x = 1; x <= 300; x++)
            {
                for (int y = 1; y <= 300; y++)
                {
                    int squarePower = GetSquarePower(x, y, 3);
                    if (squarePower > maxPower)
                    {
                        maxPower = squarePower;
                        maxPowerX = x;
                        maxPowerY = y;
                    }
                }
            }

            Console.WriteLine($"Part 1: {maxPowerX},{maxPowerY}");
        }

        static void Part2()
        {
            int maxPower = int.MinValue;
            int maxPowerX = -1;
            int maxPowerY = -1;
            int maxPowerSize = -1;
            var cache = new Dictionary<Tuple<int, int>, int>();

            for (int size = 1; size <= 300; size++)
            {
                for (int x = 1; x <= 300; x++)
                {
                    for (int y = 1; y <= 300; y++)
                    {
                        int power = GetSquarePowerWithMemoization(x, y, size, cache);
                        if (power > maxPower)
                        {
                            maxPower = power;
                            maxPowerX = x;
                            maxPowerY = y;
                            maxPowerSize = size;
                        }
                    }
                }
            }

            Console.WriteLine($"Part 2: {maxPowerX},{maxPowerY},{maxPowerSize}");
        }

        static void Main(string[] args)
        {
            Part1();
            Part2();
        }
    }
}
