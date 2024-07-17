; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

%"Node" = type {i32, %"Node"*}
declare i32 @"printf"(i8* %".1", ...)

@"nullptr" = internal global i32 0
define void @"addNode"(%"Node"* %".1", %"Node"* %".2")
{
entry:
  %".4" = getelementptr %"Node", %"Node"* %".1", i32 0, i32 1
  %".5" = load %"Node"*, %"Node"** %".4"
  store %"Node"* %".2", %"Node"** %".4"
  ret void
}

define void @"reverseLinkedList"(%"Node"** %".1")
{
entry:
  %".3" = load i32, i32* @"nullptr"
  %".4" = inttoptr i32 %".3" to %"Node"*
  %".5" = alloca %"Node"*
  store %"Node"* %".4", %"Node"** %".5"
  %".7" = load %"Node"*, %"Node"** %".1"
  %".8" = alloca %"Node"*
  store %"Node"* %".7", %"Node"** %".8"
  %".10" = alloca %"Node"*
  br label %"entryloop_do"
entryloop_do:
  br label %"entry.loop_cond"
entry.loop_cond:
  %".13" = load i32, i32* @"nullptr"
  %".14" = load %"Node"*, %"Node"** %".8"
  %".15" = ptrtoint %"Node"* %".14" to i32
  %".16" = icmp ne i32 %".15", %".13"
  br i1 %".16", label %"entry.loop_body", label %"entry.loop_end"
entry.loop_body:
  %".18" = load %"Node"*, %"Node"** %".10"
  %".19" = load %"Node"*, %"Node"** %".8"
  %".20" = getelementptr %"Node", %"Node"* %".19", i32 0, i32 1
  %".21" = load %"Node"*, %"Node"** %".20"
  store %"Node"* %".21", %"Node"** %".10"
  %".23" = load %"Node"*, %"Node"** %".8"
  %".24" = getelementptr %"Node", %"Node"* %".23", i32 0, i32 1
  %".25" = load %"Node"*, %"Node"** %".24"
  %".26" = load %"Node"*, %"Node"** %".5"
  store %"Node"* %".26", %"Node"** %".24"
  %".28" = load %"Node"*, %"Node"** %".5"
  %".29" = load %"Node"*, %"Node"** %".8"
  store %"Node"* %".29", %"Node"** %".5"
  %".31" = load %"Node"*, %"Node"** %".8"
  %".32" = load %"Node"*, %"Node"** %".10"
  store %"Node"* %".32", %"Node"** %".8"
  br label %"entry.loop_update"
entry.loop_end:
  %".36" = load %"Node"*, %"Node"** %".1"
  %".37" = load %"Node"*, %"Node"** %".5"
  store %"Node"* %".37", %"Node"** %".1"
  ret void
entry.loop_update:
  br label %"entry.loop_cond"
}

define i32 @"main"()
{
entry:
  %".2" = alloca [22 x i8]
  store [22 x i8] c"\0a=== Linked list ===\0a\00", [22 x i8]* %".2"
  %".4" = getelementptr [22 x i8], [22 x i8]* %".2", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4")
  %".6" = alloca %"Node"
  %".7" = alloca %"Node"
  %".8" = alloca %"Node"
  %".9" = getelementptr %"Node", %"Node"* %".6", i32 0, i32 0
  %".10" = getelementptr %"Node", %"Node"* %".6", i32 0, i32 0
  %".11" = load i32, i32* %".10"
  store i32 3, i32* %".10"
  %".13" = getelementptr %"Node", %"Node"* %".6", i32 0, i32 0
  %".14" = getelementptr %"Node", %"Node"* %".6", i32 0, i32 1
  %".15" = load %"Node"*, %"Node"** %".14"
  %".16" = load i32, i32* @"nullptr"
  %".17" = inttoptr i32 %".16" to %"Node"*
  store %"Node"* %".17", %"Node"** %".14"
  %".19" = getelementptr %"Node", %"Node"* %".7", i32 0, i32 0
  %".20" = getelementptr %"Node", %"Node"* %".7", i32 0, i32 0
  %".21" = load i32, i32* %".20"
  store i32 9, i32* %".20"
  %".23" = getelementptr %"Node", %"Node"* %".7", i32 0, i32 0
  %".24" = getelementptr %"Node", %"Node"* %".7", i32 0, i32 1
  %".25" = load %"Node"*, %"Node"** %".24"
  %".26" = load i32, i32* @"nullptr"
  %".27" = inttoptr i32 %".26" to %"Node"*
  store %"Node"* %".27", %"Node"** %".24"
  %".29" = getelementptr %"Node", %"Node"* %".8", i32 0, i32 0
  %".30" = getelementptr %"Node", %"Node"* %".8", i32 0, i32 0
  %".31" = load i32, i32* %".30"
  store i32 27, i32* %".30"
  %".33" = getelementptr %"Node", %"Node"* %".8", i32 0, i32 0
  %".34" = getelementptr %"Node", %"Node"* %".8", i32 0, i32 1
  %".35" = load %"Node"*, %"Node"** %".34"
  %".36" = load i32, i32* @"nullptr"
  %".37" = inttoptr i32 %".36" to %"Node"*
  store %"Node"* %".37", %"Node"** %".34"
  %".39" = getelementptr %"Node", %"Node"* %".6", i32 0, i32 0
  %".40" = getelementptr %"Node", %"Node"* %".7", i32 0, i32 0
  call void @"addNode"(%"Node"* %".6", %"Node"* %".7")
  %".42" = getelementptr %"Node", %"Node"* %".7", i32 0, i32 0
  %".43" = getelementptr %"Node", %"Node"* %".8", i32 0, i32 0
  call void @"addNode"(%"Node"* %".7", %"Node"* %".8")
  %".45" = getelementptr %"Node", %"Node"* %".6", i32 0, i32 0
  %".46" = alloca %"Node"*
  store %"Node"* %".6", %"Node"** %".46"
  %".48" = alloca [23 x i8]
  store [23 x i8] c"Original linked list:\0a\00", [23 x i8]* %".48"
  %".50" = getelementptr [23 x i8], [23 x i8]* %".48", i32 0, i32 0
  %".51" = call i32 (i8*, ...) @"printf"(i8* %".50")
  %".52" = load %"Node"*, %"Node"** %".46"
  %".53" = alloca %"Node"*
  store %"Node"* %".52", %"Node"** %".53"
  br label %"entryloop_do"
entryloop_do:
  %".56" = load %"Node"*, %"Node"** %".53"
  %".57" = getelementptr %"Node", %"Node"* %".56", i32 0, i32 0
  %".58" = load i32, i32* %".57"
  %".59" = alloca [12 x i8]
  store [12 x i8] c" data = %d\0a\00", [12 x i8]* %".59"
  %".61" = getelementptr [12 x i8], [12 x i8]* %".59", i32 0, i32 0
  %".62" = call i32 (i8*, ...) @"printf"(i8* %".61", i32 %".58")
  %".63" = load %"Node"*, %"Node"** %".53"
  %".64" = load %"Node"*, %"Node"** %".53"
  %".65" = getelementptr %"Node", %"Node"* %".64", i32 0, i32 1
  %".66" = load %"Node"*, %"Node"** %".65"
  store %"Node"* %".66", %"Node"** %".53"
  br label %"entry.loop_cond"
entry.loop_cond:
  %".69" = load i32, i32* @"nullptr"
  %".70" = load %"Node"*, %"Node"** %".53"
  %".71" = ptrtoint %"Node"* %".70" to i32
  %".72" = icmp ne i32 %".71", %".69"
  br i1 %".72", label %"entry.loop_body", label %"entry.loop_end"
entry.loop_body:
  %".74" = load %"Node"*, %"Node"** %".53"
  %".75" = getelementptr %"Node", %"Node"* %".74", i32 0, i32 0
  %".76" = load i32, i32* %".75"
  %".77" = alloca [12 x i8]
  store [12 x i8] c" data = %d\0a\00", [12 x i8]* %".77"
  %".79" = getelementptr [12 x i8], [12 x i8]* %".77", i32 0, i32 0
  %".80" = call i32 (i8*, ...) @"printf"(i8* %".79", i32 %".76")
  %".81" = load %"Node"*, %"Node"** %".53"
  %".82" = load %"Node"*, %"Node"** %".53"
  %".83" = getelementptr %"Node", %"Node"* %".82", i32 0, i32 1
  %".84" = load %"Node"*, %"Node"** %".83"
  store %"Node"* %".84", %"Node"** %".53"
  br label %"entry.loop_update"
entry.loop_end:
  %".88" = load %"Node"*, %"Node"** %".46"
  call void @"reverseLinkedList"(%"Node"** %".46")
  %".90" = alloca [24 x i8]
  store [24 x i8] c"\0aReversed linked list:\0a\00", [24 x i8]* %".90"
  %".92" = getelementptr [24 x i8], [24 x i8]* %".90", i32 0, i32 0
  %".93" = call i32 (i8*, ...) @"printf"(i8* %".92")
  %".94" = load %"Node"*, %"Node"** %".53"
  %".95" = load %"Node"*, %"Node"** %".46"
  store %"Node"* %".95", %"Node"** %".53"
  br label %"entry.loop_endloop_do"
entry.loop_update:
  br label %"entry.loop_cond"
entry.loop_endloop_do:
  %".98" = load %"Node"*, %"Node"** %".53"
  %".99" = getelementptr %"Node", %"Node"* %".98", i32 0, i32 0
  %".100" = load i32, i32* %".99"
  %".101" = alloca [12 x i8]
  store [12 x i8] c" data = %d\0a\00", [12 x i8]* %".101"
  %".103" = getelementptr [12 x i8], [12 x i8]* %".101", i32 0, i32 0
  %".104" = call i32 (i8*, ...) @"printf"(i8* %".103", i32 %".100")
  %".105" = load %"Node"*, %"Node"** %".53"
  %".106" = load %"Node"*, %"Node"** %".53"
  %".107" = getelementptr %"Node", %"Node"* %".106", i32 0, i32 1
  %".108" = load %"Node"*, %"Node"** %".107"
  store %"Node"* %".108", %"Node"** %".53"
  br label %"entry.loop_end.loop_cond"
entry.loop_end.loop_cond:
  %".111" = load i32, i32* @"nullptr"
  %".112" = load %"Node"*, %"Node"** %".53"
  %".113" = ptrtoint %"Node"* %".112" to i32
  %".114" = icmp ne i32 %".113", %".111"
  br i1 %".114", label %"entry.loop_end.loop_body", label %"entry.loop_end.loop_end"
entry.loop_end.loop_body:
  %".116" = load %"Node"*, %"Node"** %".53"
  %".117" = getelementptr %"Node", %"Node"* %".116", i32 0, i32 0
  %".118" = load i32, i32* %".117"
  %".119" = alloca [12 x i8]
  store [12 x i8] c" data = %d\0a\00", [12 x i8]* %".119"
  %".121" = getelementptr [12 x i8], [12 x i8]* %".119", i32 0, i32 0
  %".122" = call i32 (i8*, ...) @"printf"(i8* %".121", i32 %".118")
  %".123" = load %"Node"*, %"Node"** %".53"
  %".124" = load %"Node"*, %"Node"** %".53"
  %".125" = getelementptr %"Node", %"Node"* %".124", i32 0, i32 1
  %".126" = load %"Node"*, %"Node"** %".125"
  store %"Node"* %".126", %"Node"** %".53"
  br label %"entry.loop_end.loop_update"
entry.loop_end.loop_end:
  ret i32 0
entry.loop_end.loop_update:
  br label %"entry.loop_end.loop_cond"
}
