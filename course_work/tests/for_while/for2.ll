; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %".2" = alloca i32
  store i32 0, i32* %".2"
  %".4" = alloca i32
  store i32 1, i32* %".4"
  br label %"entryloop_do"
entryloop_do:
  br label %"entry.loop_cond"
entry.loop_cond:
  %".8" = load i32, i32* %".2"
  %".9" = icmp slt i32 %".8", 5
  br i1 %".9", label %"entry.loop_body", label %"entry.loop_end"
entry.loop_body:
  %".11" = load i32, i32* %".4"
  %".12" = mul i32 %".11", 3
  store i32 %".12", i32* %".4"
  %".14" = load i32, i32* %".2"
  %".15" = icmp eq i32 %".14", 2
  br i1 %".15", label %"entry.loop_body.if", label %"entry.loop_body.endif"
entry.loop_end:
  ret i32 0
entry.loop_update:
  %".37" = load i32, i32* %".2"
  %".38" = add i32 %".37", 1
  store i32 %".38", i32* %".2"
  br label %"entry.loop_cond"
entry.loop_body.if:
  %".17" = load i32, i32* %".4"
  %".18" = alloca [14 x i8]
  store [14 x i8] c"for i=2 j=%d\0a\00", [14 x i8]* %".18"
  %".20" = getelementptr [14 x i8], [14 x i8]* %".18", i32 0, i32 0
  %".21" = call i32 (i8*, ...) @"printf"(i8* %".20", i32 %".17")
  %".22" = alloca [8 x i8]
  store [8 x i8] c"break!\0a\00", [8 x i8]* %".22"
  %".24" = getelementptr [8 x i8], [8 x i8]* %".22", i32 0, i32 0
  %".25" = call i32 (i8*, ...) @"printf"(i8* %".24")
  br label %"entry.loop_end"
entry.loop_body.endif:
  %".27" = load i32, i32* %".2"
  %".28" = alloca [17 x i8]
  store [17 x i8] c"for i=%d j=NONE\0a\00", [17 x i8]* %".28"
  %".30" = getelementptr [17 x i8], [17 x i8]* %".28", i32 0, i32 0
  %".31" = call i32 (i8*, ...) @"printf"(i8* %".30", i32 %".27")
  %".32" = alloca [2 x i8]
  store [2 x i8] c"\0a\00", [2 x i8]* %".32"
  %".34" = getelementptr [2 x i8], [2 x i8]* %".32", i32 0, i32 0
  %".35" = call i32 (i8*, ...) @"printf"(i8* %".34")
  br label %"entry.loop_update"
}
