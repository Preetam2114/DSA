#include <bits/stdc++.h>

using namespace std;

#ifndef preetam
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC target ("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,avx2,tune=native")
#endif

#define F first
#define S second 
#define pb push_back 
#define mp make_pair
#define rep(i,a,b) for(int i = a; i <= b; i++)
#define inputarr(arr,n) for(int i = 0; i < n; i++) cin>>arr[i];
#define inputmat(arr,a,b) for(int i=0; i < a; i++)for(int j=0; j < b; j++)cin>>arr[i][j];
#define print(arr) for(auto a:arr) cout<<a<<" "; cout<<"\n";
#define all(ar) ar.begin(), ar.end()
#define foreach(it, ar) for (auto it = ar.begin(); it != ar.end(); it++)
#define fil(ar, val) memset(ar, val, sizeof(ar))
#define endl '\n'

#ifndef preetam
template<typename KeyType, typename ValueType> 
std::pair<KeyType,ValueType> get_max( const std::map<KeyType,ValueType>& x ) {
  using pairtype=std::pair<KeyType,ValueType>; 
  return *std::max_element(x.begin(), x.end(), [] (const pairtype & p1, const pairtype & p2) {
        return p1.second < p2.second;
  }); 
}

template <class Container>
void split(const std::string& str, Container& cont){
    std::istringstream iss(str);
    std::copy(std::istream_iterator<std::string>(iss),
         std::istream_iterator<std::string>(),
         std::back_inserter(cont));
}

constexpr unsigned int shash(const char *s, int off = 0){                        
    return !s[off] ? 5381 : (shash(s, off+1)*33) ^ s[off];                           
}

typedef long long ll;
typedef long double ld;
typedef long double f80;
typedef pair<int, int> pii;
const ll mod = 1e9;
#endif

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
  int t, n, m[21][21], cnt[1001][21][21];
	cin >> t;
	while(t--){
		cin >> n;
		for (int i = 1; i <= 1000; i++) {
			for (int j = 0; j <= n; j++) {
				for (int k = 0; k <= n; k++) {
					cnt[i][j][k] = 0;
				}
			}
		}

		for (int i = 0; i <= n; i++) {
			m[n][i] = 0;
			m[i][n] = 0;
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cin >> m[i][j];
			}
		}

		for (int i = 1; i <= 1000; i++) {
			for (int j = n - 1; j >= 0; j--) {
				for (int k = n - 1; k >= 0; k--) {
					cnt[i][j][k] = cnt[i][j][k+1] + cnt[i][j+1][k] - cnt[i][j+1][k+1] + (i == m[j][k] ? 1 : 0);
				}
			}
		}

		int inv = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				for (int k = 1; k < m[i][j]; k++) {
					inv += cnt[k][i][j];
				}
			}
		}

		cout << inv << endl;
	}
	return 0;
}