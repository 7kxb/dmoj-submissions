#[macro_use] extern crate dmoj;
fn main() {
    let mut ans = 91;
    let a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    ans += a[scan!(usize)] * 1;
    ans += a[scan!(usize)] * 3;
    ans += a[scan!(usize)] * 1;
    println!("The 1-3-sum is {}", ans);
}