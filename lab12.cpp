#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <queue>
#include <iostream>

using namespace std;

vector<string> split_and_sort(const string &input_file, size_t chunk_size)
{
    ifstream in(input_file);
    vector<string> temp_files;
    vector<int> chunk;
    int x;
    size_t idx = 0;

    while (in >> x)
    {
        chunk.push_back(x);
        if (chunk.size() >= chunk_size)
        {
            sort(chunk.begin(), chunk.end());
            string fname = "chunk_" + to_string(idx++) + ".txt";
            ofstream out(fname);
            for (int v : chunk)
                out << v << "\n";
            out.close();
            temp_files.push_back(fname);
            chunk.clear();
        }
    }
    if (!chunk.empty())
    {
        std::sort(chunk.begin(), chunk.end());
        string fname = "chunk_" + to_string(idx++) + ".txt";
        ofstream out(fname);
        for (int v : chunk)
            out << v << "\n";
        out.close();
        temp_files.push_back(fname);
    }
    return temp_files;
}

void merge_files(const vector<string> &files, const string &output_file)
{
    struct Node
    {
        int value, idx;
        bool operator>(const Node &other) const
        {
            return value > other.value;
        }
    };

    vector<ifstream> inputs(files.size());
    for (size_t i = 0; i < files.size(); i++)
    {
        inputs[i].open(files[i]);
    }

    priority_queue<Node, vector<Node>, greater<Node>> pq;
    for (size_t i = 0; i < inputs.size(); i++)
    {
        int val;
        if (inputs[i] >> val)
        {
            pq.push({val, (int)i});
        }
    }

    ofstream out(output_file);
    while (!pq.empty())
    {
        auto [val, idx] = pq.top();
        pq.pop();
        out << val << "\n";
        int next_val;
        if (inputs[idx] >> next_val)
        {
            pq.push({next_val, idx});
        }
    }
    out.close();
    for (auto &f : inputs)
        f.close();
}

int main()
{
    auto chunks = split_and_sort("lab12/input.txt", 10);
    merge_files(chunks, "lab12/sorted_output.txt");
    for (auto &f : chunks)
        remove(f.c_str());
    return 0;
}
