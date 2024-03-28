#include<bits/stdc++.h>
using namespace std;
const int n=3;
unordered_map<string,bool>vis;

int pd(int x,int y) {
    if(x<0||x>2||y<0||y>2) return 0;
    return 1;
}
int d[4][3]={{-1,0},{1,0},{0,-1},{0,1}};
struct Node {
    string v;
    int step;
};
queue<Node>q;
char t[128];
int main(){
    freopen("data_c.txt","r",stdin);
    freopen("submission.txt","w",stdout);
    string s,aim="012345678";
    while(cin.getline(t,128)) {
        vis.clear();
        while(!q.empty()) q.pop();
        s="";
        for(int i=0;i<strlen(t);i++) {
            if(isdigit(t[i])) s += t[i];
        }
        q.push({s,0});
        while(!q.empty()) {
            Node p=q.front();
            q.pop();
            if(p.v==aim) {
                cout<<p.step<<endl;
                break;
            }
            if(vis[p.v]) continue;
            vis[p.v]=1;
            for(int i=0;i<n;i++) {
                for(int j=0;j<n;j++) {
                    if(p.v[i*n+j]=='8') {
                        for(int k=0;k<4;k++) {
                            int nx = (i+d[k][0]);
                            if(nx<0) nx += 3;
                            if(nx>=3) nx -= 3;
                            int ny = j+d[k][1];
                            if(ny<0) ny += 3;
                            if(ny>=3) ny -= 3;
                            swap(p.v[i*n+j],p.v[nx*n+ny]);
                            q.push({p.v,p.step+1});
                            swap(p.v[i*n+j],p.v[nx*n+ny]);
                        }
                    }
                }
            }
        }

    }
}
