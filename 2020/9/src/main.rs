use std::fs;
use combinations::Combinations;


fn main() {
    let contents = fs::read_to_string("input.txt").expect(
        "Something went wrong reading the file",
    );
    let input: Vec<i64> = contents.lines().map(|x| { x.parse::<i64>().unwrap() }).collect();
    let mut x = 0i64;
    for i in 25..input.len() {
        let mut combinations = Vec::new();
        for combination in Combinations::new(input[i-25..i].to_vec(), 2) {
            combinations.push(combination.iter().sum::<i64>());
        }
        x = input[i];
        if !combinations.contains(&x) {
            break;
        }
    }
    println!("Part 1: {}", x);
    let mut num = Vec::new();
    let mut index = 0;
    loop {
        let mut sum = num.iter().sum::<i64>();
        if sum == x {
            println!("Break");
            break;
        }
        if sum > x {
            num.remove(0);
        } else if sum < x {
            num.push(input[index]);
            index += 1;
        }
    }
    let min: i64 = *num.iter().min().unwrap();
    let max: i64 = *num.iter().max().unwrap();
    println!("Part 2: {:?}", min + max);
}
