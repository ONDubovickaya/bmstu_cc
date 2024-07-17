; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"if_func"(i32 %".1")
{
entry:
  %".3" = alloca i32
  store i32 0, i32* %".3"
  %".5" = icmp eq i32 %".1", 1
  br i1 %".5", label %"entry.if", label %"entry.else"
entry.if:
  %".7" = load i32, i32* %".3"
  store i32 1, i32* %".3"
  br label %"entry.endif"
entry.else:
  %".10" = icmp eq i32 %".1", 2
  br i1 %".10", label %"entry.else.if", label %"entry.else.else"
entry.endif:
  %".30" = load i32, i32* %".3"
  ret i32 %".30"
entry.else.if:
  %".12" = load i32, i32* %".3"
  store i32 2, i32* %".3"
  br label %"entry.else.endif"
entry.else.else:
  %".15" = icmp sge i32 %".1", 3
  br i1 %".15", label %"entry.else.else.if", label %"entry.else.else.endif"
entry.else.endif:
  br label %"entry.endif"
entry.else.else.if:
  %".17" = load i32, i32* %".3"
  store i32 3, i32* %".3"
  %".19" = icmp eq i32 %".1", 4
  br i1 %".19", label %"entry.else.else.if.if", label %"entry.else.else.if.else"
entry.else.else.endif:
  br label %"entry.else.endif"
entry.else.else.if.if:
  %".21" = load i32, i32* %".3"
  store i32 4, i32* %".3"
  br label %"entry.else.else.if.endif"
entry.else.else.if.else:
  %".24" = load i32, i32* %".3"
  store i32 5, i32* %".3"
  br label %"entry.else.else.if.endif"
entry.else.else.if.endif:
  br label %"entry.else.else.endif"
}

define void @"test"()
{
entry:
  %".2" = alloca [12 x i8]
  store [12 x i8] c"Testing if:\00", [12 x i8]* %".2"
  %".4" = getelementptr [12 x i8], [12 x i8]* %".2", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4")
  %".6" = alloca i32
  store i32 0, i32* %".6"
  br label %"entryloop_do"
entryloop_do:
  br label %"entry.loop_cond"
entry.loop_cond:
  %".10" = load i32, i32* %".6"
  %".11" = icmp slt i32 %".10", 5
  br i1 %".11", label %"entry.loop_body", label %"entry.loop_end"
entry.loop_body:
  %".13" = load i32, i32* %".6"
  %".14" = call i32 @"if_func"(i32 %".13")
  %".15" = alloca [5 x i8]
  store [5 x i8] c" %d \00", [5 x i8]* %".15"
  %".17" = getelementptr [5 x i8], [5 x i8]* %".15", i32 0, i32 0
  %".18" = call i32 (i8*, ...) @"printf"(i8* %".17", i32 %".14")
  br label %"entry.loop_update"
entry.loop_end:
  %".24" = alloca [2 x i8]
  store [2 x i8] c"\0a\00", [2 x i8]* %".24"
  %".26" = getelementptr [2 x i8], [2 x i8]* %".24", i32 0, i32 0
  %".27" = call i32 (i8*, ...) @"printf"(i8* %".26")
  ret void
entry.loop_update:
  %".20" = load i32, i32* %".6"
  %".21" = add i32 %".20", 1
  store i32 %".21", i32* %".6"
  br label %"entry.loop_cond"
}

define i32 @"main"()
{
entry:
  call void @"test"()
  ret i32 0
}
