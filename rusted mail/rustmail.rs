use regex::Regex;
//A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pattern.
fn main() 
{
let re : Regex = Regex::new( re r"^([a-zA-z0-9_\-\.]+)@([a-zA-z0-9_\-\.])\.([a-zA-Z]{2,5})$").unwrap();//these are random combinations of numbers,patterns and alphabets.
if(re.is_match(text: "example@gmail.com")){}//checks whether valid or invalid
println!("This is a valid email");
}
else{
	println(" This is an invalid account ")
}
}
