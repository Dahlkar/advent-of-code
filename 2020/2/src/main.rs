use std::fs;


fn main() {
    let contents = fs::read_to_string("input.txt").expect(
        "Something went wrong reading the file",
    );
    let passwords:Vec<((i32, i32), char, &str)> = contents.lines().map(|x| {
        let row:Vec<&str> = x.split(' ').collect();
        let num:Vec<&str> = row[0].split('-').collect();
        let letter = row[1].chars().next().unwrap();
        let password = row[2];
        ((num[0].parse::<i32>().unwrap(), num[1].parse::<i32>().unwrap()), letter, password)
    }).collect();
    let mut correct = 0i32;
    for ((low, high), letter, password) in passwords.clone() {
        let num_chars = password.matches(letter).count() as i32;
        if low <= num_chars && num_chars <= high {
            correct += 1;
        }
    }
    println!("part 1: {}", correct);
    let mut correct = 0i32;
    for ((i, j), letter, password) in passwords.clone() {
        let ci = password.chars().nth((i-1) as usize).unwrap();
        let cj = password.chars().nth((j-1) as usize).unwrap();
        if (ci == letter) != (cj == letter) {
            correct += 1;
        }
    }
    println!("part 2: {}", correct);
}
