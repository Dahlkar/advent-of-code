use std::fs;
use std::fmt;
use std::collections::HashMap;


static REQUIRED_KEYS: &'static [&str] = &[
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
];

static VALID_EYE_COLORS: &'static [&str] = &[
    "amb",
    "blu",
    "brn",
    "gry",
    "grn",
    "hzl",
    "oth",
];


struct Passport {
    pairs: HashMap<String, String>,
}

impl Passport {
    pub fn new(entries: String) -> Passport {
        let mut pairs = HashMap::new();
        entries
            .split(' ')
            .filter(|entry| { !entry.trim().is_empty() })
            .for_each(|entry| {
                let bits = entry.split(':').collect::<Vec<&str>>();
                pairs.insert(bits[0].to_string(), bits[1].to_string());
            });
        Passport { pairs }
    }

    pub fn to_string(&self) -> String {
        self.pairs
            .iter()
            .map(|pair| {
                format!("{}:{}", pair.0, pair.1)
            })
            .collect::<Vec<String>>()
            .join(", ")
    }

    pub fn is_valid(&self, extended: bool) -> bool {
        for key in REQUIRED_KEYS {
            if !self.pairs.contains_key(&key.to_string()) {
                return false
            }
        }
        if extended {
            for (k, v) in self.pairs.iter() {
                match k.as_str() {
                    "byr" | "iyr" | "eyr" => {
                        let year = v.parse::<i32>().unwrap();
                        match k.as_str() {
                            "byr" if 1920 <= year && year <= 2002 => {},
                            "iyr" if 2010 <= year && year <= 2020 => {},
                            "eyr" if 2020 <= year && year <= 2030 => {},
                            _ => return false,
                        }
                    }
                    "hgt" => {
                        let height = v[0..v.len()-2].parse::<i32>().unwrap_or(0);
                        match &v[v.len()-2..] {
                            "cm" if 150 <= height && height <= 193 => {},
                            "in" if 59 <= height && height <= 76 => {},
                            _ => return false,
                        }
                    }
                    "hcl" if v.starts_with('#') || v.len() == 7 => {
                        match i32::from_str_radix(&v[1..], 16) {
                            Ok(_) => {},
                            _ => return false,
                        }
                    }
                    "ecl" if VALID_EYE_COLORS.contains(&v.as_str()) => {},
                    "pid" if v.len() == 9 => {
                        match v.parse::<i32>() {
                            Ok(_) => {},
                            _ => return false,
                        }
                    }
                    "cid" => {},
                    _ => {
                        return false
                    }
                };
            }
        }
        true
    }
}

impl fmt::Display for Passport {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{}", self.to_string())
    }
}

fn main() {
    let contents = fs::read_to_string("input.txt").expect(
        "Something went wrong reading the file",
    );
    let passports = contents
        .split("\n\n")
        .map(|entry| { Passport::new(entry.replace("\n", " ")) })
        .collect::<Vec<Passport>>();
    let part_1 = passports.iter().filter(|passport| { passport.is_valid(false)}).count();
    println!("Part 1: {}", part_1);
    let part_2 = passports.iter().filter(|passport| { passport.is_valid(true)}).count();
    println!("Part 2: {}", part_2);
}
