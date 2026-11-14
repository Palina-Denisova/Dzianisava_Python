## Task 2. Bracket sequence

**Given sequence:** [((())()(())]]

**1. Can this sequence be considered correct?**

No. The sequence is incorrect because the brackets are not properly matched and nested.

**2. What needs to be changed to make it correct?**

Replace the penultimate closing square bracket `]` with a closing parenthesis `)`.

**Corrected sequence:**
`[((())()(()))]`

**3. **Validation logic:**

To check bracket sequences, I used the following principles:

1. **Matching pairs:** Each opening bracket must have a corresponding closing bracket of the same type.
2. **Correct nesting order:** Brackets must be closed in the reverse order in which they were opened (LIFO — Last In, First Out).
3. **Balanced brackets:** The number of opening and closing brackets of each type must be equal.
4. **No unmatched brackets:** All brackets must be properly closed by the end of the sequence.