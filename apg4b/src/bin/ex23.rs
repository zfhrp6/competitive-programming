use proconio::input;
use std::collections::HashMap;

fn main() {
    input! {
        n: usize,
        a: [usize; n],
    }

    let mut map: HashMap<usize, usize> = HashMap::new();
    for c in a {
        if map.contains_key(&c) {
            *map.get_mut(&c).unwrap() = map.get(&c).unwrap() + 1;
        } else {
            map.insert(c, 1);
        }
    }

    let (mut max_number, mut max_count): (usize, usize) = (0, 0);
    for item in map.iter() {
        if max_count < *item.1 {
            max_count = *item.1;
            max_number = *item.0;
        }
    }
    println!("{} {}", max_number, max_count);
}
