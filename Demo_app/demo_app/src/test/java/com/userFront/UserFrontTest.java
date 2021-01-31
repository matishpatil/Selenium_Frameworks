package com.userFront;

import static org.junit.Assert.assertEquals;

import org.junit.Test;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
public class UserFrontTest {
	
	@Test
	public void successTest() {
		
		String s="success";
		assertEquals("success",s);
		
	}
	
	@Test(expected = AssertionError.class)
	public void failureTest() {
		
		String s=null;
		assertEquals("success",s);
		
	}

}
