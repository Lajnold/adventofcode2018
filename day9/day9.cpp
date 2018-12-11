#include <algorithm>
#include <fstream>
#include <iostream>
#include <list>
#include <vector>

using namespace std;

struct GameDef
{
    int num_players;
    int last_marble;

    GameDef(int num_players, int last_marble)
    {
        this->num_players = num_players;
        this->last_marble = last_marble;
    }
};

GameDef load_game_def()
{
    // 416 players; last marble is worth 71617 points
    ifstream file("input.txt");
    int num_players;
    int last_marble;
    string ignore;
    file >> num_players >> ignore >> ignore >> ignore >> ignore >> ignore >> last_marble;
    return GameDef(num_players, last_marble);
}

void change_position(list<int>& marbles, list<int>::iterator& iterator, int n)
{
    if (n > 0)
    {
        while (n--)
        {
            ++iterator;
            if (iterator == marbles.end())
            {
                iterator = marbles.begin();
            }
        }
    }
    else
    {
        while (n++)
        {
            if (iterator == marbles.begin())
            {
                iterator = marbles.end();
                --iterator;
            }
            else
            {
                --iterator;
            }
        }
    }
}

vector<unsigned long long> run_game(int num_players, int last_marble)
{
    vector<unsigned long long> scores(num_players);
    list<int> marbles = { 0 };
    int cur_player = 0;
    int cur_marble = 1;
    auto cur_position = marbles.begin();

    while (cur_marble <= last_marble)
    {
        if (cur_marble % 23 == 0)
        {
            scores[cur_player] += cur_marble;
            change_position(marbles, cur_position, -7);
            scores[cur_player] += *cur_position;
            cur_position = marbles.erase(cur_position);
            if (cur_position == marbles.end())
            {
                cur_position = marbles.begin();
            }
        }
        else
        {
            if (marbles.size() == 1)
            {
                cur_position = marbles.end();
            }
            else
            {
                change_position(marbles, cur_position, 2);
            }

            cur_position = marbles.insert(cur_position, cur_marble);
        }

        cur_player = (cur_player + 1) % num_players;
        cur_marble++;
    }

    return scores;
}

void part1()
{
    GameDef game_def = load_game_def();
    auto scores = run_game(game_def.num_players, game_def.last_marble);
    cout << "Part 1: " << *max_element(scores.begin(), scores.end()) << endl;
}

void part2()
{
    GameDef game_def = load_game_def();
    auto scores = run_game(game_def.num_players, game_def.last_marble * 100);
    cout << "Part 2: " << *max_element(scores.begin(), scores.end()) << endl;
}

int main()
{
    part1();
    part2();
    return 0;
}