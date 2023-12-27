use std::fs;
use std::collections::HashSet;
use std::iter::FromIterator;


fn main() {
    let contents = fs::read_to_string("input.txt").expect(
        "Something went wrong reading the file",
    );
    let part_1: Vec<i32> = contents
        .split("\n\n")
        .map(|x| { HashSet::<char>::from_iter(x.replace('\n', "").chars().collect::<Vec<char>>()).len() as i32})
        .collect();
    println!("{:?}", part_1.iter().sum::<i32>());
    let part_2: Vec<i32> = contents
        .split("\n\n")
        .map(|x| {
            let lines = x.lines().collect::<Vec<&str>>();
            let members = lines.len();
            let answers = x.replace('\n', "");
            let questions = HashSet::<char>::from_iter(answers.chars().collect::<Vec<char>>());
            questions.iter().filter( |c| {
                answers.match_indices(**c).count() == members
            }).count() as i32
        })
        .collect();
    println!("{:?}", part_2.iter().sum::<i32>());
}
