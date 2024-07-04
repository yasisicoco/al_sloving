function solution(a) {
  let ans = new Array(a.length).fill(false);
  let s_val = Infinity;
  let e_val = Infinity;

  for (let i = 0; i < a.length; i++) {
    if (a[i] < s_val) {
      s_val = a[i];
      ans[i] = true;
    }
    if (a[a.length - 1 - i] < e_val) {
      e_val = a[a.length - 1 - i];
      ans[a.length - 1 - i] = true;
    }
  }
  return ans.filter(Boolean).length;
}