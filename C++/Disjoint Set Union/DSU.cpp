#include<iostream>
#include<bits/stdc++.h>
using namespace std;

static int fast_io = []() { std::ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr); return 0; }();

class DSU {
	vector<int> parent, size;
public:
	DSU(int n) {
		parent.resize(n, 0);
		for(int i = 0; i < n; i++) parent[i] = i;
		size.resize(n, 1);
	}
	int find(int x) {
		if(parent[x] == x)
			return x;
		return parent[x] = find(parent[x]);
	}
	void merge(int u, int v) {
		int a = find(u), b = find(v);
		if(a != b) {
			if(size[a] > size[b]) {
				parent[b] = a;
				size[a] += size[b];
			} else {
				parent[a] = b;
				size[b] += size[a];
			}
		}
	}
};