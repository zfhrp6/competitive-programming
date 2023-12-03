use proconio::input;

fn main() {
    input! {
        n: usize,
    }

    let mut pos = (0, 0);
    let mut now = 0;
    for _ in 0..n {
        input! {
            t: usize,
            x: usize,
            y: usize,
        }

        let d = distance(pos, (x,y));
        let d_t = t - now;
        // 次に移動する距離が、次の時刻までの時間より大きいと移動が間に合わない
        if d > d_t {
            println!("No");
            std::process::exit(0);
        }

        // 毎回移動する必要があるので、移動距離と移動時間の奇偶は一致する。一致しなければ無理
        if d_t%2 != d%2 {
            println!("No");
            std::process::exit(0);
        }

        pos = (x,y);
        now = t;
    }
    println!("Yes");
}

// 距離はマンハッタンで
fn distance(s: (usize, usize), t: (usize, usize)) -> usize {
    let x_dif = if s.0 > t.0 { s.0 - t.0 } else { t.0 - s.0 };
    let y_dif = if s.1 > t.1 { s.1 - t.1 } else { t.1 - s.1 };
    x_dif + y_dif
}
