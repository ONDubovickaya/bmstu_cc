; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %".2" = sub i32 0, 5
  %".3" = alloca i32
  store i32 %".2", i32* %".3"
  %".5" = alloca i32
  store i32 17, i32* %".5"
  %".7" = load i32, i32* %".3"
  %".8" = icmp sgt i32 %".7", 0
  %".9" = alloca i1
  br i1 %".8", label %"entry.if", label %"entry.else"
entry.if:
  %".11" = load i32, i32* %".5"
  %".12" = icmp sgt i32 %".11", 0
  store i1 %".12", i1* %".9"
  br label %"entry.endif"
entry.else:
  store i1 0, i1* %".9"
  br label %"entry.endif"
entry.endif:
  %".17" = load i1, i1* %".9"
  br i1 %".17", label %"entry.endif.if", label %"entry.endif.else"
entry.endif.if:
  %".19" = alloca [33 x i8]
  store [33 x i8] c"Both x and y are greater than 0\0a\00", [33 x i8]* %".19"
  %".21" = getelementptr [33 x i8], [33 x i8]* %".19", i32 0, i32 0
  %".22" = call i32 (i8*, ...) @"printf"(i8* %".21")
  br label %"entry.endif.endif"
entry.endif.else:
  %".24" = load i32, i32* %".3"
  %".25" = icmp sgt i32 %".24", 0
  br i1 %".25", label %"entry.endif.else.if", label %"entry.endif.else.else"
entry.endif.endif:
  %".47" = load i32, i32* %".3"
  %".48" = icmp slt i32 %".47", 10
  %".49" = alloca i1
  br i1 %".48", label %"entry.endif.endif.if", label %"entry.endif.endif.else"
entry.endif.else.if:
  %".27" = alloca [21 x i8]
  store [21 x i8] c"x is greater than 0\0a\00", [21 x i8]* %".27"
  %".29" = getelementptr [21 x i8], [21 x i8]* %".27", i32 0, i32 0
  %".30" = call i32 (i8*, ...) @"printf"(i8* %".29")
  br label %"entry.endif.else.endif"
entry.endif.else.else:
  %".32" = load i32, i32* %".5"
  %".33" = icmp sgt i32 %".32", 0
  br i1 %".33", label %"entry.endif.else.else.if", label %"entry.endif.else.else.else"
entry.endif.else.endif:
  br label %"entry.endif.endif"
entry.endif.else.else.if:
  %".35" = alloca [21 x i8]
  store [21 x i8] c"y is greater than 0\0a\00", [21 x i8]* %".35"
  %".37" = getelementptr [21 x i8], [21 x i8]* %".35", i32 0, i32 0
  %".38" = call i32 (i8*, ...) @"printf"(i8* %".37")
  br label %"entry.endif.else.else.endif"
entry.endif.else.else.else:
  %".40" = alloca [33 x i8]
  store [33 x i8] c"Both x and y are smaller than 0\0a\00", [33 x i8]* %".40"
  %".42" = getelementptr [33 x i8], [33 x i8]* %".40", i32 0, i32 0
  %".43" = call i32 (i8*, ...) @"printf"(i8* %".42")
  br label %"entry.endif.else.else.endif"
entry.endif.else.else.endif:
  br label %"entry.endif.else.endif"
entry.endif.endif.if:
  store i1 1, i1* %".49"
  br label %"entry.endif.endif.endif"
entry.endif.endif.else:
  %".53" = load i32, i32* %".5"
  %".54" = icmp slt i32 %".53", 10
  store i1 %".54", i1* %".49"
  br label %"entry.endif.endif.endif"
entry.endif.endif.endif:
  %".57" = load i1, i1* %".49"
  br i1 %".57", label %"entry.endif.endif.endif.if", label %"entry.endif.endif.endif.endif"
entry.endif.endif.endif.if:
  %".59" = alloca [40 x i8]
  store [40 x i8] c"At least one of x or y is less than 10\0a\00", [40 x i8]* %".59"
  %".61" = getelementptr [40 x i8], [40 x i8]* %".59", i32 0, i32 0
  %".62" = call i32 (i8*, ...) @"printf"(i8* %".61")
  br label %"entry.endif.endif.endif.endif"
entry.endif.endif.endif.endif:
  ret i32 0
}
