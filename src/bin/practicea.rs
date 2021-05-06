use whiteread::parse_line;

fn main() {
    let a: i32 = parse_line().unwrap();
    let (b, c): (i32, i32) = parse_line().unwrap();
    let s: String = parse_line().unwrap();

    println!("{} {}", a + b + c, s);
}
