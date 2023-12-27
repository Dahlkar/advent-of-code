use std::fs;
use combinations::Combinations;

fn solve(entries: Vec<i32>, num_entries: usize) -> Option<i32> {
    let combinations = Combinations::new(entries, num_entries);
    for combination in combinations {
        if combination.iter().sum::<i32>() == 2020 {
            return Some(combination.iter().product::<i32>());
        }
    }
    None
}

fn main() {
    let contents = fs::read_to_string("input.txt").expect(
        "Something went wrong reading the file",
    );
    let entries: Vec<i32> = contents.lines().map(|x| { x.parse::<i32>().unwrap() }).collect();
    let part_1 = solve(entries.clone(), 2);
    println!("{}", part_1.unwrap());
    let part_2 = solve(entries.clone(), 3);
    println!("{}", part_2.unwrap());
}
