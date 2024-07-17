# Generated from antlr_parser/TinyC.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TinyCParser import TinyCParser
else:
    from TinyCParser import TinyCParser

# This class defines a complete listener for a parse tree produced by TinyCParser.
class TinyCListener(ParseTreeListener):

    # Enter a parse tree produced by TinyCParser#compilationUnit.
    def enterCompilationUnit(self, ctx:TinyCParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by TinyCParser#compilationUnit.
    def exitCompilationUnit(self, ctx:TinyCParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by TinyCParser#translationUnit.
    def enterTranslationUnit(self, ctx:TinyCParser.TranslationUnitContext):
        pass

    # Exit a parse tree produced by TinyCParser#translationUnit.
    def exitTranslationUnit(self, ctx:TinyCParser.TranslationUnitContext):
        pass


    # Enter a parse tree produced by TinyCParser#externalDeclaration.
    def enterExternalDeclaration(self, ctx:TinyCParser.ExternalDeclarationContext):
        pass

    # Exit a parse tree produced by TinyCParser#externalDeclaration.
    def exitExternalDeclaration(self, ctx:TinyCParser.ExternalDeclarationContext):
        pass


    # Enter a parse tree produced by TinyCParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:TinyCParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by TinyCParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:TinyCParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by TinyCParser#declarationList.
    def enterDeclarationList(self, ctx:TinyCParser.DeclarationListContext):
        pass

    # Exit a parse tree produced by TinyCParser#declarationList.
    def exitDeclarationList(self, ctx:TinyCParser.DeclarationListContext):
        pass


    # Enter a parse tree produced by TinyCParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:TinyCParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by TinyCParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:TinyCParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by TinyCParser#genericSelection.
    def enterGenericSelection(self, ctx:TinyCParser.GenericSelectionContext):
        pass

    # Exit a parse tree produced by TinyCParser#genericSelection.
    def exitGenericSelection(self, ctx:TinyCParser.GenericSelectionContext):
        pass


    # Enter a parse tree produced by TinyCParser#genericAssocList.
    def enterGenericAssocList(self, ctx:TinyCParser.GenericAssocListContext):
        pass

    # Exit a parse tree produced by TinyCParser#genericAssocList.
    def exitGenericAssocList(self, ctx:TinyCParser.GenericAssocListContext):
        pass


    # Enter a parse tree produced by TinyCParser#genericAssociation.
    def enterGenericAssociation(self, ctx:TinyCParser.GenericAssociationContext):
        pass

    # Exit a parse tree produced by TinyCParser#genericAssociation.
    def exitGenericAssociation(self, ctx:TinyCParser.GenericAssociationContext):
        pass


    # Enter a parse tree produced by TinyCParser#postfixExpression.
    def enterPostfixExpression(self, ctx:TinyCParser.PostfixExpressionContext):
        pass

    # Exit a parse tree produced by TinyCParser#postfixExpression.
    def exitPostfixExpression(self, ctx:TinyCParser.PostfixExpressionContext):
        pass


    # Enter a parse tree produced by TinyCParser#argumentExpressionList.
    def enterArgumentExpressionList(self, ctx:TinyCParser.ArgumentExpressionListContext):
        pass

    # Exit a parse tree produced by TinyCParser#argumentExpressionList.
    def exitArgumentExpressionList(self, ctx:TinyCParser.ArgumentExpressionListContext):
        pass


    # Enter a parse tree produced by TinyCParser#unaryExpression.
    def enterUnaryExpression(self, ctx:TinyCParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by TinyCParser#unaryExpression.
    def exitUnaryExpression(self, ctx:TinyCParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by TinyCParser#unaryOperator.
    def enterUnaryOperator(self, ctx:TinyCParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by TinyCParser#unaryOperator.
    def exitUnaryOperator(self, ctx:TinyCParser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by TinyCParser#castExpression.
    def enterCastExpression(self, ctx:TinyCParser.CastExpressionContext):
        pass

    # Exit a parse tree produced by TinyCParser#castExpression.
    def exitCastExpression(self, ctx:TinyCParser.CastExpressionContext):
        pass


    # Enter a parse tree produced by TinyCParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:TinyCParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by TinyCParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:TinyCParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by TinyCParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:TinyCParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by TinyCParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:TinyCParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by TinyCParser#shiftExpression.
    def enterShiftExpression(self, ctx:TinyCParser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by TinyCParser#shiftExpression.
    def exitShiftExpression(self, ctx:TinyCParser.ShiftExpressionContext):
        pass


    # Enter a parse tree produced by TinyCParser#relationalExpression.
    def enterRelationalExpression(self, ctx:TinyCParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by TinyCParser#relationalExpression.
    def exitRelationalExpression(self, ctx:TinyCParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by TinyCParser#equalityExpression.
    def enterEqualityExpression(self, ctx:TinyCParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by TinyCParser#equalityExpression.
    def exitEqualityExpression(self, ctx:TinyCParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by TinyCParser#andExpression.
    def enterAndExpression(self, ctx:TinyCParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by TinyCParser#andExpression.
    def exitAndExpression(self, ctx:TinyCParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by TinyCParser#exclusiveOrExpression.
    def enterExclusiveOrExpression(self, ctx:TinyCParser.ExclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by TinyCParser#exclusiveOrExpression.
    def exitExclusiveOrExpression(self, ctx:TinyCParser.ExclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by TinyCParser#inclusiveOrExpression.
    def enterInclusiveOrExpression(self, ctx:TinyCParser.InclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by TinyCParser#inclusiveOrExpression.
    def exitInclusiveOrExpression(self, ctx:TinyCParser.InclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by TinyCParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:TinyCParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by TinyCParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:TinyCParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by TinyCParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:TinyCParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by TinyCParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:TinyCParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by TinyCParser#conditionalExpression.
    def enterConditionalExpression(self, ctx:TinyCParser.ConditionalExpressionContext):
        pass

    # Exit a parse tree produced by TinyCParser#conditionalExpression.
    def exitConditionalExpression(self, ctx:TinyCParser.ConditionalExpressionContext):
        pass


    # Enter a parse tree produced by TinyCParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:TinyCParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by TinyCParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:TinyCParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by TinyCParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:TinyCParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by TinyCParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:TinyCParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by TinyCParser#expression.
    def enterExpression(self, ctx:TinyCParser.ExpressionContext):
        pass

    # Exit a parse tree produced by TinyCParser#expression.
    def exitExpression(self, ctx:TinyCParser.ExpressionContext):
        pass


    # Enter a parse tree produced by TinyCParser#constantExpression.
    def enterConstantExpression(self, ctx:TinyCParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by TinyCParser#constantExpression.
    def exitConstantExpression(self, ctx:TinyCParser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by TinyCParser#declaration.
    def enterDeclaration(self, ctx:TinyCParser.DeclarationContext):
        pass

    # Exit a parse tree produced by TinyCParser#declaration.
    def exitDeclaration(self, ctx:TinyCParser.DeclarationContext):
        pass


    # Enter a parse tree produced by TinyCParser#declarationSpecifiers.
    def enterDeclarationSpecifiers(self, ctx:TinyCParser.DeclarationSpecifiersContext):
        pass

    # Exit a parse tree produced by TinyCParser#declarationSpecifiers.
    def exitDeclarationSpecifiers(self, ctx:TinyCParser.DeclarationSpecifiersContext):
        pass


    # Enter a parse tree produced by TinyCParser#declarationSpecifiers2.
    def enterDeclarationSpecifiers2(self, ctx:TinyCParser.DeclarationSpecifiers2Context):
        pass

    # Exit a parse tree produced by TinyCParser#declarationSpecifiers2.
    def exitDeclarationSpecifiers2(self, ctx:TinyCParser.DeclarationSpecifiers2Context):
        pass


    # Enter a parse tree produced by TinyCParser#declarationSpecifier.
    def enterDeclarationSpecifier(self, ctx:TinyCParser.DeclarationSpecifierContext):
        pass

    # Exit a parse tree produced by TinyCParser#declarationSpecifier.
    def exitDeclarationSpecifier(self, ctx:TinyCParser.DeclarationSpecifierContext):
        pass


    # Enter a parse tree produced by TinyCParser#initDeclaratorList.
    def enterInitDeclaratorList(self, ctx:TinyCParser.InitDeclaratorListContext):
        pass

    # Exit a parse tree produced by TinyCParser#initDeclaratorList.
    def exitInitDeclaratorList(self, ctx:TinyCParser.InitDeclaratorListContext):
        pass


    # Enter a parse tree produced by TinyCParser#initDeclarator.
    def enterInitDeclarator(self, ctx:TinyCParser.InitDeclaratorContext):
        pass

    # Exit a parse tree produced by TinyCParser#initDeclarator.
    def exitInitDeclarator(self, ctx:TinyCParser.InitDeclaratorContext):
        pass


    # Enter a parse tree produced by TinyCParser#storageClassSpecifier.
    def enterStorageClassSpecifier(self, ctx:TinyCParser.StorageClassSpecifierContext):
        pass

    # Exit a parse tree produced by TinyCParser#storageClassSpecifier.
    def exitStorageClassSpecifier(self, ctx:TinyCParser.StorageClassSpecifierContext):
        pass


    # Enter a parse tree produced by TinyCParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:TinyCParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by TinyCParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:TinyCParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by TinyCParser#structOrUnionSpecifier.
    def enterStructOrUnionSpecifier(self, ctx:TinyCParser.StructOrUnionSpecifierContext):
        pass

    # Exit a parse tree produced by TinyCParser#structOrUnionSpecifier.
    def exitStructOrUnionSpecifier(self, ctx:TinyCParser.StructOrUnionSpecifierContext):
        pass


    # Enter a parse tree produced by TinyCParser#structOrUnion.
    def enterStructOrUnion(self, ctx:TinyCParser.StructOrUnionContext):
        pass

    # Exit a parse tree produced by TinyCParser#structOrUnion.
    def exitStructOrUnion(self, ctx:TinyCParser.StructOrUnionContext):
        pass


    # Enter a parse tree produced by TinyCParser#structDeclarationList.
    def enterStructDeclarationList(self, ctx:TinyCParser.StructDeclarationListContext):
        pass

    # Exit a parse tree produced by TinyCParser#structDeclarationList.
    def exitStructDeclarationList(self, ctx:TinyCParser.StructDeclarationListContext):
        pass


    # Enter a parse tree produced by TinyCParser#structDeclaration.
    def enterStructDeclaration(self, ctx:TinyCParser.StructDeclarationContext):
        pass

    # Exit a parse tree produced by TinyCParser#structDeclaration.
    def exitStructDeclaration(self, ctx:TinyCParser.StructDeclarationContext):
        pass


    # Enter a parse tree produced by TinyCParser#specifierQualifierList.
    def enterSpecifierQualifierList(self, ctx:TinyCParser.SpecifierQualifierListContext):
        pass

    # Exit a parse tree produced by TinyCParser#specifierQualifierList.
    def exitSpecifierQualifierList(self, ctx:TinyCParser.SpecifierQualifierListContext):
        pass


    # Enter a parse tree produced by TinyCParser#structDeclaratorList.
    def enterStructDeclaratorList(self, ctx:TinyCParser.StructDeclaratorListContext):
        pass

    # Exit a parse tree produced by TinyCParser#structDeclaratorList.
    def exitStructDeclaratorList(self, ctx:TinyCParser.StructDeclaratorListContext):
        pass


    # Enter a parse tree produced by TinyCParser#structDeclarator.
    def enterStructDeclarator(self, ctx:TinyCParser.StructDeclaratorContext):
        pass

    # Exit a parse tree produced by TinyCParser#structDeclarator.
    def exitStructDeclarator(self, ctx:TinyCParser.StructDeclaratorContext):
        pass


    # Enter a parse tree produced by TinyCParser#enumSpecifier.
    def enterEnumSpecifier(self, ctx:TinyCParser.EnumSpecifierContext):
        pass

    # Exit a parse tree produced by TinyCParser#enumSpecifier.
    def exitEnumSpecifier(self, ctx:TinyCParser.EnumSpecifierContext):
        pass


    # Enter a parse tree produced by TinyCParser#enumeratorList.
    def enterEnumeratorList(self, ctx:TinyCParser.EnumeratorListContext):
        pass

    # Exit a parse tree produced by TinyCParser#enumeratorList.
    def exitEnumeratorList(self, ctx:TinyCParser.EnumeratorListContext):
        pass


    # Enter a parse tree produced by TinyCParser#enumerator.
    def enterEnumerator(self, ctx:TinyCParser.EnumeratorContext):
        pass

    # Exit a parse tree produced by TinyCParser#enumerator.
    def exitEnumerator(self, ctx:TinyCParser.EnumeratorContext):
        pass


    # Enter a parse tree produced by TinyCParser#enumerationConstant.
    def enterEnumerationConstant(self, ctx:TinyCParser.EnumerationConstantContext):
        pass

    # Exit a parse tree produced by TinyCParser#enumerationConstant.
    def exitEnumerationConstant(self, ctx:TinyCParser.EnumerationConstantContext):
        pass


    # Enter a parse tree produced by TinyCParser#atomicTypeSpecifier.
    def enterAtomicTypeSpecifier(self, ctx:TinyCParser.AtomicTypeSpecifierContext):
        pass

    # Exit a parse tree produced by TinyCParser#atomicTypeSpecifier.
    def exitAtomicTypeSpecifier(self, ctx:TinyCParser.AtomicTypeSpecifierContext):
        pass


    # Enter a parse tree produced by TinyCParser#typeQualifier.
    def enterTypeQualifier(self, ctx:TinyCParser.TypeQualifierContext):
        pass

    # Exit a parse tree produced by TinyCParser#typeQualifier.
    def exitTypeQualifier(self, ctx:TinyCParser.TypeQualifierContext):
        pass


    # Enter a parse tree produced by TinyCParser#functionSpecifier.
    def enterFunctionSpecifier(self, ctx:TinyCParser.FunctionSpecifierContext):
        pass

    # Exit a parse tree produced by TinyCParser#functionSpecifier.
    def exitFunctionSpecifier(self, ctx:TinyCParser.FunctionSpecifierContext):
        pass


    # Enter a parse tree produced by TinyCParser#alignmentSpecifier.
    def enterAlignmentSpecifier(self, ctx:TinyCParser.AlignmentSpecifierContext):
        pass

    # Exit a parse tree produced by TinyCParser#alignmentSpecifier.
    def exitAlignmentSpecifier(self, ctx:TinyCParser.AlignmentSpecifierContext):
        pass


    # Enter a parse tree produced by TinyCParser#declarator.
    def enterDeclarator(self, ctx:TinyCParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by TinyCParser#declarator.
    def exitDeclarator(self, ctx:TinyCParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by TinyCParser#directDeclarator.
    def enterDirectDeclarator(self, ctx:TinyCParser.DirectDeclaratorContext):
        pass

    # Exit a parse tree produced by TinyCParser#directDeclarator.
    def exitDirectDeclarator(self, ctx:TinyCParser.DirectDeclaratorContext):
        pass


    # Enter a parse tree produced by TinyCParser#gccDeclaratorExtension.
    def enterGccDeclaratorExtension(self, ctx:TinyCParser.GccDeclaratorExtensionContext):
        pass

    # Exit a parse tree produced by TinyCParser#gccDeclaratorExtension.
    def exitGccDeclaratorExtension(self, ctx:TinyCParser.GccDeclaratorExtensionContext):
        pass


    # Enter a parse tree produced by TinyCParser#gccAttributeSpecifier.
    def enterGccAttributeSpecifier(self, ctx:TinyCParser.GccAttributeSpecifierContext):
        pass

    # Exit a parse tree produced by TinyCParser#gccAttributeSpecifier.
    def exitGccAttributeSpecifier(self, ctx:TinyCParser.GccAttributeSpecifierContext):
        pass


    # Enter a parse tree produced by TinyCParser#gccAttributeList.
    def enterGccAttributeList(self, ctx:TinyCParser.GccAttributeListContext):
        pass

    # Exit a parse tree produced by TinyCParser#gccAttributeList.
    def exitGccAttributeList(self, ctx:TinyCParser.GccAttributeListContext):
        pass


    # Enter a parse tree produced by TinyCParser#gccAttribute.
    def enterGccAttribute(self, ctx:TinyCParser.GccAttributeContext):
        pass

    # Exit a parse tree produced by TinyCParser#gccAttribute.
    def exitGccAttribute(self, ctx:TinyCParser.GccAttributeContext):
        pass


    # Enter a parse tree produced by TinyCParser#nestedParenthesesBlock.
    def enterNestedParenthesesBlock(self, ctx:TinyCParser.NestedParenthesesBlockContext):
        pass

    # Exit a parse tree produced by TinyCParser#nestedParenthesesBlock.
    def exitNestedParenthesesBlock(self, ctx:TinyCParser.NestedParenthesesBlockContext):
        pass


    # Enter a parse tree produced by TinyCParser#pointer.
    def enterPointer(self, ctx:TinyCParser.PointerContext):
        pass

    # Exit a parse tree produced by TinyCParser#pointer.
    def exitPointer(self, ctx:TinyCParser.PointerContext):
        pass


    # Enter a parse tree produced by TinyCParser#typeQualifierList.
    def enterTypeQualifierList(self, ctx:TinyCParser.TypeQualifierListContext):
        pass

    # Exit a parse tree produced by TinyCParser#typeQualifierList.
    def exitTypeQualifierList(self, ctx:TinyCParser.TypeQualifierListContext):
        pass


    # Enter a parse tree produced by TinyCParser#parameterTypeList.
    def enterParameterTypeList(self, ctx:TinyCParser.ParameterTypeListContext):
        pass

    # Exit a parse tree produced by TinyCParser#parameterTypeList.
    def exitParameterTypeList(self, ctx:TinyCParser.ParameterTypeListContext):
        pass


    # Enter a parse tree produced by TinyCParser#parameterList.
    def enterParameterList(self, ctx:TinyCParser.ParameterListContext):
        pass

    # Exit a parse tree produced by TinyCParser#parameterList.
    def exitParameterList(self, ctx:TinyCParser.ParameterListContext):
        pass


    # Enter a parse tree produced by TinyCParser#parameterDeclaration.
    def enterParameterDeclaration(self, ctx:TinyCParser.ParameterDeclarationContext):
        pass

    # Exit a parse tree produced by TinyCParser#parameterDeclaration.
    def exitParameterDeclaration(self, ctx:TinyCParser.ParameterDeclarationContext):
        pass


    # Enter a parse tree produced by TinyCParser#identifierList.
    def enterIdentifierList(self, ctx:TinyCParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by TinyCParser#identifierList.
    def exitIdentifierList(self, ctx:TinyCParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by TinyCParser#typeName.
    def enterTypeName(self, ctx:TinyCParser.TypeNameContext):
        pass

    # Exit a parse tree produced by TinyCParser#typeName.
    def exitTypeName(self, ctx:TinyCParser.TypeNameContext):
        pass


    # Enter a parse tree produced by TinyCParser#abstractDeclarator.
    def enterAbstractDeclarator(self, ctx:TinyCParser.AbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by TinyCParser#abstractDeclarator.
    def exitAbstractDeclarator(self, ctx:TinyCParser.AbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by TinyCParser#directAbstractDeclarator.
    def enterDirectAbstractDeclarator(self, ctx:TinyCParser.DirectAbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by TinyCParser#directAbstractDeclarator.
    def exitDirectAbstractDeclarator(self, ctx:TinyCParser.DirectAbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by TinyCParser#typedefName.
    def enterTypedefName(self, ctx:TinyCParser.TypedefNameContext):
        pass

    # Exit a parse tree produced by TinyCParser#typedefName.
    def exitTypedefName(self, ctx:TinyCParser.TypedefNameContext):
        pass


    # Enter a parse tree produced by TinyCParser#initializer.
    def enterInitializer(self, ctx:TinyCParser.InitializerContext):
        pass

    # Exit a parse tree produced by TinyCParser#initializer.
    def exitInitializer(self, ctx:TinyCParser.InitializerContext):
        pass


    # Enter a parse tree produced by TinyCParser#initializerList.
    def enterInitializerList(self, ctx:TinyCParser.InitializerListContext):
        pass

    # Exit a parse tree produced by TinyCParser#initializerList.
    def exitInitializerList(self, ctx:TinyCParser.InitializerListContext):
        pass


    # Enter a parse tree produced by TinyCParser#designation.
    def enterDesignation(self, ctx:TinyCParser.DesignationContext):
        pass

    # Exit a parse tree produced by TinyCParser#designation.
    def exitDesignation(self, ctx:TinyCParser.DesignationContext):
        pass


    # Enter a parse tree produced by TinyCParser#designatorList.
    def enterDesignatorList(self, ctx:TinyCParser.DesignatorListContext):
        pass

    # Exit a parse tree produced by TinyCParser#designatorList.
    def exitDesignatorList(self, ctx:TinyCParser.DesignatorListContext):
        pass


    # Enter a parse tree produced by TinyCParser#designator.
    def enterDesignator(self, ctx:TinyCParser.DesignatorContext):
        pass

    # Exit a parse tree produced by TinyCParser#designator.
    def exitDesignator(self, ctx:TinyCParser.DesignatorContext):
        pass


    # Enter a parse tree produced by TinyCParser#staticAssertDeclaration.
    def enterStaticAssertDeclaration(self, ctx:TinyCParser.StaticAssertDeclarationContext):
        pass

    # Exit a parse tree produced by TinyCParser#staticAssertDeclaration.
    def exitStaticAssertDeclaration(self, ctx:TinyCParser.StaticAssertDeclarationContext):
        pass


    # Enter a parse tree produced by TinyCParser#statement.
    def enterStatement(self, ctx:TinyCParser.StatementContext):
        pass

    # Exit a parse tree produced by TinyCParser#statement.
    def exitStatement(self, ctx:TinyCParser.StatementContext):
        pass


    # Enter a parse tree produced by TinyCParser#labeledStatement.
    def enterLabeledStatement(self, ctx:TinyCParser.LabeledStatementContext):
        pass

    # Exit a parse tree produced by TinyCParser#labeledStatement.
    def exitLabeledStatement(self, ctx:TinyCParser.LabeledStatementContext):
        pass


    # Enter a parse tree produced by TinyCParser#compoundStatement.
    def enterCompoundStatement(self, ctx:TinyCParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by TinyCParser#compoundStatement.
    def exitCompoundStatement(self, ctx:TinyCParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by TinyCParser#blockItemList.
    def enterBlockItemList(self, ctx:TinyCParser.BlockItemListContext):
        pass

    # Exit a parse tree produced by TinyCParser#blockItemList.
    def exitBlockItemList(self, ctx:TinyCParser.BlockItemListContext):
        pass


    # Enter a parse tree produced by TinyCParser#blockItem.
    def enterBlockItem(self, ctx:TinyCParser.BlockItemContext):
        pass

    # Exit a parse tree produced by TinyCParser#blockItem.
    def exitBlockItem(self, ctx:TinyCParser.BlockItemContext):
        pass


    # Enter a parse tree produced by TinyCParser#expressionStatement.
    def enterExpressionStatement(self, ctx:TinyCParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by TinyCParser#expressionStatement.
    def exitExpressionStatement(self, ctx:TinyCParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by TinyCParser#selectionStatement.
    def enterSelectionStatement(self, ctx:TinyCParser.SelectionStatementContext):
        pass

    # Exit a parse tree produced by TinyCParser#selectionStatement.
    def exitSelectionStatement(self, ctx:TinyCParser.SelectionStatementContext):
        pass


    # Enter a parse tree produced by TinyCParser#iterationStatement.
    def enterIterationStatement(self, ctx:TinyCParser.IterationStatementContext):
        pass

    # Exit a parse tree produced by TinyCParser#iterationStatement.
    def exitIterationStatement(self, ctx:TinyCParser.IterationStatementContext):
        pass


    # Enter a parse tree produced by TinyCParser#forCondition.
    def enterForCondition(self, ctx:TinyCParser.ForConditionContext):
        pass

    # Exit a parse tree produced by TinyCParser#forCondition.
    def exitForCondition(self, ctx:TinyCParser.ForConditionContext):
        pass


    # Enter a parse tree produced by TinyCParser#forDeclaration.
    def enterForDeclaration(self, ctx:TinyCParser.ForDeclarationContext):
        pass

    # Exit a parse tree produced by TinyCParser#forDeclaration.
    def exitForDeclaration(self, ctx:TinyCParser.ForDeclarationContext):
        pass


    # Enter a parse tree produced by TinyCParser#forExpression.
    def enterForExpression(self, ctx:TinyCParser.ForExpressionContext):
        pass

    # Exit a parse tree produced by TinyCParser#forExpression.
    def exitForExpression(self, ctx:TinyCParser.ForExpressionContext):
        pass


    # Enter a parse tree produced by TinyCParser#jumpStatement.
    def enterJumpStatement(self, ctx:TinyCParser.JumpStatementContext):
        pass

    # Exit a parse tree produced by TinyCParser#jumpStatement.
    def exitJumpStatement(self, ctx:TinyCParser.JumpStatementContext):
        pass



del TinyCParser