import java.util.HashSet;
import java.util.Set;

public class PropositionalLogic {
    public static String proposition = "0";
    public String getProposition() {
        String prop = proposition;
        proposition = new String(Integer.parseInt(proposition) + 1 + "");
        return prop;
    }
    public Set<String> reason(Set<String> theorems) {
        Set<String> reasoning = new HashSet<String>();
        //Addition
        for (String theoremA : theorems) {
            for (String theoremB : theorems) {
                reasoning.add("<" + theoremA + "^" + theoremB + ">");
            }
        }
        //Separation
        for (String theorem : theorems) {
            if (isOperation(theorem, '^') && theorem.charAt(0) == '<') {
                int index = indexOfOperation(theorem, '^');
                String leftArg = theorem.substring(theorem.indexOf('<') + 1, index);
                String rightArg = theorem.substring(index + 1, theorem.length() - 1);
                reasoning.add(leftArg);
                reasoning.add(rightArg);
            }
        }
        //Double Negation
        for (String theorem : theorems) {
            reasoning.add("~~" + theorem);
            for (int i = 0; i < numOccurences(theorem, "~~"); i++) {
                reasoning.add(removeOccurence(theorem, "~~", i));
            }
        }
//        //Fantasy
//        Set<String> assumptions = //....
//        Set<String> subTheorems = new HashSet<String>().addAll(theorems).addAll(assumptions);
//        Set<String> conclusions = reason(subTheorems);
//        for (String assumption : assumptions) {
//            for (String conclusion : conclusions) {
//                theorems.add("<" + assumption + "}" + conclusion + ">";
//            }
//        }
        //Contraposition
        for (String theorem : theorems) {
            if (isOperation(theorem, '}')) {
                int index = indexOfOperation(theorem, '}');
                String leftArg = theorem.substring(theorem.indexOf('<') + 1, index);
                String rightArg = theorem.substring(index + 1, theorem.length() - 1);
                reasoning.add(theorem.substring(0, theorem.indexOf('<')) + "<~" + rightArg + "}~" + leftArg + ">");
            }
        }
        //Rule of Detachment
        for (String theoremA : theorems) {
            for (String theoremB : theorems) {
                if (isOperation(theoremB, '}') && theoremB.charAt(0) == '<') {
                    int index = indexOfOperation(theoremB, '}');
                    String leftArg = theoremB.substring(theoremB.indexOf('<') + 1, index);
                    if (leftArg.equals(theoremA)) {
                        String rightArg = theoremB.substring(index + 1, theoremB.length() - 1);
                        reasoning.add(rightArg);
                    }
                }
            }
        }
        //DeMorgan
        for (String theorem : theorems) {
            //Distribute Negation
            if (theorem.charAt(0) != '<') {
                if (isOperation(theorem,'^')) {
                    int index = indexOfOperation(theorem, '^');
                    String leftArg = theorem.substring(theorem.indexOf('<') + 1, index);
                    String rightArg = theorem.substring(index + 1, theorem.length() - 1);
                    reasoning.add(theorem.substring(0, theorem.indexOf('<') - 1) + "<~" + leftArg + "v~" + rightArg + ">");
                } else if (isOperation(theorem,'v')) {
                    int index = indexOfOperation(theorem, 'v');
                    String leftArg = theorem.substring(theorem.indexOf('<') + 1, index);
                    String rightArg = theorem.substring(index + 1, theorem.length() - 1);
                    reasoning.add(theorem.substring(0, theorem.indexOf('<') - 1) + "<~" + leftArg + "^~" + rightArg + ">");
                }
            }
            //Factor Out Negation
            if (isOperation(theorem,'^')) {
                int index = indexOfOperation(theorem, '^');
                String leftArg = theorem.substring(theorem.indexOf('<') + 1, index);
                String rightArg = theorem.substring(index + 1, theorem.length() - 1);
                if (leftArg.charAt(0) == '~' && rightArg.charAt(0) == '~') {
                    reasoning.add(theorem.substring(0, theorem.indexOf('<')) + "~<" + leftArg.substring(1, leftArg.length()) + "v" + rightArg.substring(1, rightArg.length()) + ">");
                }
            } else if (isOperation(theorem,'v')) {
                int index = indexOfOperation(theorem, 'v');
                String leftArg = theorem.substring(theorem.indexOf('<') + 1, index);
                String rightArg = theorem.substring(index + 1, theorem.length() - 1);
                if (leftArg.charAt(0) == '~' && rightArg.charAt(0) == '~') {
                    reasoning.add(theorem.substring(0, theorem.indexOf('<')) + "~<" + leftArg.substring(1, leftArg.length()) + "^" + rightArg.substring(1, rightArg.length()) + ">");
                }
            }
        }
        //Material Implication
        for (String theorem : theorems) {
            if (isOperation(theorem, '}')) {
                int index = indexOfOperation(theorem, '}');
                String leftArg = theorem.substring(theorem.indexOf('<') + 1, index);
                String rightArg = theorem.substring(index + 1, theorem.length() - 1);
                reasoning.add(theorem.substring(0, theorem.indexOf('<')) + "<~" + leftArg + "v" + rightArg + ">");
            }
            else if (isOperation(theorem, 'v')) {
                int index = indexOfOperation(theorem, 'v');
                String leftArg = theorem.substring(theorem.indexOf('<') + 1, index);
                String rightArg = theorem.substring(index + 1, theorem.length() - 1);
                reasoning.add(theorem.substring(0, theorem.indexOf('<')) + "<~" + leftArg + "}" + rightArg + ">");
            }
        }
        return reasoning;
    }
    public static boolean isOperation(String theorem, char operation) {
        int backAngleCount = 0;
        for (int index = 0; index < theorem.length(); index++) {
            if (theorem.charAt(index) == '<') {
                backAngleCount++;
            } else if (theorem.charAt(index) == '>') {
                backAngleCount--;
            } else if (theorem.charAt(index) == operation && backAngleCount == 1) {
                return true;
            }
        }
        return false;
    }
    public static int indexOfOperation(String theorem, char operation) {
        int backAngleCount = 0;
        for (int index = 0; index < theorem.length(); index++) {
            if (theorem.charAt(index) == '<') {
                backAngleCount++;
            } else if (theorem.charAt(index) == '>') {
                backAngleCount--;
            } else if (theorem.charAt(index) == operation && backAngleCount == 1) {
                return index;
            }
        }
        return -1;
    }
    public static int numOccurences(String string, String substring) {
        int count = 0;
        for (int i = 0; i < string.length() - substring.length(); i++) {
            String currentSection = string.substring(i, i + substring.length());
            if (currentSection.equals(substring)) {
                count++;
            }
        }
        return count;
    }
    public static String removeOccurence(String string, String substring, int occurenceIndex) {
        int currentIndex = 0;
        for (int i = 0; i < string.length() - substring.length(); i++) {
            String currentSection = string.substring(i, i + substring.length());
            if (currentSection.equals(substring) && occurenceIndex == currentIndex++) {
                String left = string.substring(0, i);
                String right = string.substring(i + substring.length(), string.length());
                return left + right;
            }
        }
        return string;
    }
}