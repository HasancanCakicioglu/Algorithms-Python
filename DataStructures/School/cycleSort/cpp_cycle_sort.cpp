#include <iostream>
#include <vector>

using namespace std;

void cycleSort(vector<int>& arr) {
    int n = arr.size();
    for (int start = 0; start < n - 1; start++) {
        int item = arr[start];
        int pos = start;
        for (int i = start + 1; i < n; i++) {
            if (arr[i] < item) {
                pos++;
            }
        }
        if (pos == start) {
            continue;
        }
        while (item == arr[pos]) {
            pos++;
        }
        if (pos != start) {
            swap(item, arr[pos]);
        }
        while (pos != start) {
            pos = start;
            for (int i = start + 1; i < n; i++) {
                if (arr[i] < item) {
                    pos++;
                }
            }
            while (item == arr[pos]) {
                pos++;
            }
            if (item != arr[pos]) {
                swap(item, arr[pos]);
            }
        }
    }
}

int main() {
    vector<int> arr = {10, 3, 2, 5, 56, 43, 23, 12};

    cycleSort(arr);

    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
