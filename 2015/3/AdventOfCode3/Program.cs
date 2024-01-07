using System.Security.AccessControl;
using System.Text.RegularExpressions;
using System.Collections.Generic;
using System.Net;
using System.IO;
using System;

class Program
{
    static int FirstChallenge(string instructions, Dictionary<char, (int, int)> movesMap)
    {
        int x = 0, y = 0;
        HashSet<(int, int)> houseVisited = new HashSet<(int, int)> { (0, 0) };
        foreach (char direction in instructions)
        {
            (int, int) move = movesMap[direction];
            x += move.Item1;
            y += move.Item2;
            houseVisited.Add((x, y));
        }
        return houseVisited.Count;
    }

    static int SecondChallenge(string instructions, Dictionary<char, (int, int)> movesMap)
    {
        int sx = 0, sy = 0;
        HashSet<(int, int)> houseVisitedBySanta = new HashSet<(int, int)> { (0, 0) };
        int rx = 0, ry = 0;
        HashSet<(int, int)> houseVisitedByRoboSanta = new HashSet<(int, int)> { (0, 0) };
        for (int i = 0; i < instructions.Length; i++)
        {
            (int, int) move = movesMap[instructions[i]];
            if (i % 2 == 0)
            {
                sx += move.Item1;
                sy += move.Item2;
                houseVisitedBySanta.Add((sx, sy));
            }
            else
            {  // Is an instruction for Robo-Santa
                rx += move.Item1;
                ry += move.Item2;
                houseVisitedByRoboSanta.Add((rx, ry));
            }

        }
        houseVisitedBySanta.UnionWith(houseVisitedByRoboSanta);
        return houseVisitedBySanta.Count;
    }
    static void Main()
    {
        try
        {
            string instructions = File.ReadAllText("input.txt");

            Dictionary<char, (int, int)> movesMap = new Dictionary<char, (int, int)>
            {
                {'^', (0, 1)},
                {'v', (0, -1)},
                {'<', (-1, 0)},
                {'>', (1, 0)}

            };
            int housesWithPresentF = FirstChallenge(instructions, movesMap);
            Console.WriteLine("Challenge 1: At least " + housesWithPresentF + " houses receive 1 present");

            int housesWithPresentS = SecondChallenge(instructions, movesMap);
            Console.WriteLine("Challenge 2: At least " + housesWithPresentS + " houses receive 1 present");
        }
        catch (Exception ex)
        {
            Console.WriteLine("Unexpected error:" + ex.Message);
        }
    }
}