use whiteread::parse_line;

fn main() {
    let s: String = parse_line().unwrap();
    println!("{}", s.matches("1").count());
}
