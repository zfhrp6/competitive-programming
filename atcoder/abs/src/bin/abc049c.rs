use proconio::input;

fn main() {
    input! {
        mut s: String,
    }

    let p1: String = "dream".chars().rev().collect();
    let p2: String = "dreamer".chars().rev().collect();
    let p3: String = "erase".chars().rev().collect();
    let p4: String = "eraser".chars().rev().collect();
    let patterns = vec![p1, p2, p3, p4];

    let mut s_rev: String = s.chars().rev().collect();

    while is_prefixed(&s_rev, &patterns) {
        s_rev = remove_prefix(s_rev, &patterns)
    }

    println!("{}", if s_rev == "" { "YES" } else { "NO" });
}

fn remove_prefix(s: String, pat: &Vec<String>) -> String {
    for p in pat.iter() {
        if s.starts_with(p) {
            return s.replacen(p, "", 1);
        }
    }
    s
}

fn is_prefixed(s: &str, pat: &Vec<String>) -> bool {
    for p in pat.iter() {
        if s.starts_with(p) {
            return true;
        }
    }
    false
}
