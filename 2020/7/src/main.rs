use std::fs;
use std::collections::HashMap;
use std::collections::hash_map::Iter;

struct Rules {
    rules: HashMap<String, i32>,
}

struct Bags {
    bags: HashMap<String, Rules>,
}

impl Bags {
    pub fn new(contents: &str) -> Bags {
        let mut bags = HashMap::new();
        contents
            .lines()
            .for_each(|x| {
                let rule = x.split(" bags contain").collect::<Vec<&str>>();
                bags.insert(rule[0].to_string(), Rules::new(rule[1]));
            });
        Bags { bags }
    }

    pub fn count_bags(&self, bag: &str) -> i32{
        let mut sum = 0;
        let sub_bags = self.get(bag);

        if sub_bags.is_empty() {
            return sum;
        }

        for (color, count) in sub_bags.iter() {
            sum += count;
            sum += count * self.count_bags(color);
        }
        return sum;
    }

    pub fn get(&self, key: &str) -> &Rules {
        return self.bags.get(key).unwrap();
    }
}

impl Rules {
    pub fn new(contents: &str) -> Rules {
        let mut rules = HashMap::new();
        contents
            .split(',')
            .for_each(|x| {
                if !x.contains("no other bags.") {
                    let parts = x.trim().split(' ').collect::<Vec<&str>>();
                    let count: i32 = parts[0].parse().unwrap();
                    let bag: String = parts[1..=2].join(" ").to_string();
                    rules.insert(bag, count);
                }
            });
        Rules { rules }
    }
    pub fn get(&self, key: &str) -> i32 {
        return *self.rules.get(key).unwrap();
    }
    pub fn iter(&self) -> Iter<'_, String, i32> {
        return self.rules.iter();
    }
    pub fn is_empty(&self) -> bool {
        return self.rules.is_empty();
    }
}


fn find<'a>(contents: &'a str, filter: &str ) -> Vec<&'a str> {
    return contents
        .lines()
        .filter(|x| { x.contains(filter)})
        .map(|x| {
            let rule = x.split(" bags contain").collect::<Vec<&str>>();
            rule[0]
        }).collect::<Vec<&str>>();
}


fn main() {
    let contents = fs::read_to_string("input.txt").expect(
        "Something went wrong reading the file",
    );

    let mut filters = Vec::new();
    let mut part_1 = 0i32;
    filters.push("shiny gold");
    let mut i = 0;
    while i < filters.len() {
        let found: Vec<&str> = find(&contents, filters[i]);
        for f in found {
            if !filters.contains(&f) {
                filters.push(f);
                part_1 += 1;
            }
        }
        i += 1;
    }
    let bags = Bags::new(&contents);
    println!("Part 1: {:?}", part_1);
    println!("Part 2: {}", bags.count_bags("shiny gold"));
}
