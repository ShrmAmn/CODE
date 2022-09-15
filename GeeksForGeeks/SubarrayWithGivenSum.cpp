#include<bits/stdc++.h>
using namespace std;

vector<int> SubArrayWithGivenSum( vector<int> &arr , int n , long long s )
{
      vector<int> ans;
        
      int i = 0;
      int j = 0;
      int flag = 0;
      int sum = arr[0];

      if( s == 0)
      {
          ans.push_back(-1);
          return ans;
      }

      while( i < n and j < n )
      {
          if( sum == s )
          {
              flag = 1;
              ans.push_back(i+1);
              ans.push_back(j+1);
              break;
          }
          else if( sum > s)
          {
              sum -= arr[i];
              i++;
          }
          else
          {
              j++;
              sum += arr[j];
          }
      }
      if( flag == 0 )
          ans.push_back(-1);

      return ans;
}

int main()
{
  int n ;
  cin>>n ;
  
  vector<int> v(n);
  for(int i = 0; i<n; ++i)
  {
    cin>>v[i];
  }
  
  long long s;
  cin>>s;
  
  vector<int> ans;
  ans = SubArrayWithGivenSum(v,n,s);
  
  return 0;
}
