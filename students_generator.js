JG.repeat(1, {
	students: JG.repeat(100, 150, {
		id: JG.objectId(),
		courses: _.uniq(JG.repeat(2, 10, {
			name: JG.random('MATH-121', 'CIS-121', 'CIS-122', 'CIS-223'),
			grade: JG.random("A", "A-", "B+", "B", "B-"),
			credits: 4,
		})),
	})
});
