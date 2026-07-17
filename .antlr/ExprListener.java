// Generated from c:/Users/spide/OneDrive/Escritorio/Analizador/Analizador/Expr.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ExprParser}.
 */
public interface ExprListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ExprParser#file_}.
	 * @param ctx the parse tree
	 */
	void enterFile_(ExprParser.File_Context ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#file_}.
	 * @param ctx the parse tree
	 */
	void exitFile_(ExprParser.File_Context ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#interactive}.
	 * @param ctx the parse tree
	 */
	void enterInteractive(ExprParser.InteractiveContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#interactive}.
	 * @param ctx the parse tree
	 */
	void exitInteractive(ExprParser.InteractiveContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#eval_}.
	 * @param ctx the parse tree
	 */
	void enterEval_(ExprParser.Eval_Context ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#eval_}.
	 * @param ctx the parse tree
	 */
	void exitEval_(ExprParser.Eval_Context ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#func_type}.
	 * @param ctx the parse tree
	 */
	void enterFunc_type(ExprParser.Func_typeContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#func_type}.
	 * @param ctx the parse tree
	 */
	void exitFunc_type(ExprParser.Func_typeContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#statements}.
	 * @param ctx the parse tree
	 */
	void enterStatements(ExprParser.StatementsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#statements}.
	 * @param ctx the parse tree
	 */
	void exitStatements(ExprParser.StatementsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(ExprParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(ExprParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#single_compound_stmt}.
	 * @param ctx the parse tree
	 */
	void enterSingle_compound_stmt(ExprParser.Single_compound_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#single_compound_stmt}.
	 * @param ctx the parse tree
	 */
	void exitSingle_compound_stmt(ExprParser.Single_compound_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#statement_newline}.
	 * @param ctx the parse tree
	 */
	void enterStatement_newline(ExprParser.Statement_newlineContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#statement_newline}.
	 * @param ctx the parse tree
	 */
	void exitStatement_newline(ExprParser.Statement_newlineContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#simple_stmts}.
	 * @param ctx the parse tree
	 */
	void enterSimple_stmts(ExprParser.Simple_stmtsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#simple_stmts}.
	 * @param ctx the parse tree
	 */
	void exitSimple_stmts(ExprParser.Simple_stmtsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#simple_stmt}.
	 * @param ctx the parse tree
	 */
	void enterSimple_stmt(ExprParser.Simple_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#simple_stmt}.
	 * @param ctx the parse tree
	 */
	void exitSimple_stmt(ExprParser.Simple_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#compound_stmt}.
	 * @param ctx the parse tree
	 */
	void enterCompound_stmt(ExprParser.Compound_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#compound_stmt}.
	 * @param ctx the parse tree
	 */
	void exitCompound_stmt(ExprParser.Compound_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(ExprParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(ExprParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#annotated_rhs}.
	 * @param ctx the parse tree
	 */
	void enterAnnotated_rhs(ExprParser.Annotated_rhsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#annotated_rhs}.
	 * @param ctx the parse tree
	 */
	void exitAnnotated_rhs(ExprParser.Annotated_rhsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#augassign}.
	 * @param ctx the parse tree
	 */
	void enterAugassign(ExprParser.AugassignContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#augassign}.
	 * @param ctx the parse tree
	 */
	void exitAugassign(ExprParser.AugassignContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#return_stmt}.
	 * @param ctx the parse tree
	 */
	void enterReturn_stmt(ExprParser.Return_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#return_stmt}.
	 * @param ctx the parse tree
	 */
	void exitReturn_stmt(ExprParser.Return_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#raise_stmt}.
	 * @param ctx the parse tree
	 */
	void enterRaise_stmt(ExprParser.Raise_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#raise_stmt}.
	 * @param ctx the parse tree
	 */
	void exitRaise_stmt(ExprParser.Raise_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#pass_stmt}.
	 * @param ctx the parse tree
	 */
	void enterPass_stmt(ExprParser.Pass_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#pass_stmt}.
	 * @param ctx the parse tree
	 */
	void exitPass_stmt(ExprParser.Pass_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#break_stmt}.
	 * @param ctx the parse tree
	 */
	void enterBreak_stmt(ExprParser.Break_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#break_stmt}.
	 * @param ctx the parse tree
	 */
	void exitBreak_stmt(ExprParser.Break_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#continue_stmt}.
	 * @param ctx the parse tree
	 */
	void enterContinue_stmt(ExprParser.Continue_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#continue_stmt}.
	 * @param ctx the parse tree
	 */
	void exitContinue_stmt(ExprParser.Continue_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#global_stmt}.
	 * @param ctx the parse tree
	 */
	void enterGlobal_stmt(ExprParser.Global_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#global_stmt}.
	 * @param ctx the parse tree
	 */
	void exitGlobal_stmt(ExprParser.Global_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#nonlocal_stmt}.
	 * @param ctx the parse tree
	 */
	void enterNonlocal_stmt(ExprParser.Nonlocal_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#nonlocal_stmt}.
	 * @param ctx the parse tree
	 */
	void exitNonlocal_stmt(ExprParser.Nonlocal_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#del_stmt}.
	 * @param ctx the parse tree
	 */
	void enterDel_stmt(ExprParser.Del_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#del_stmt}.
	 * @param ctx the parse tree
	 */
	void exitDel_stmt(ExprParser.Del_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#yield_stmt}.
	 * @param ctx the parse tree
	 */
	void enterYield_stmt(ExprParser.Yield_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#yield_stmt}.
	 * @param ctx the parse tree
	 */
	void exitYield_stmt(ExprParser.Yield_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#assert_stmt}.
	 * @param ctx the parse tree
	 */
	void enterAssert_stmt(ExprParser.Assert_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#assert_stmt}.
	 * @param ctx the parse tree
	 */
	void exitAssert_stmt(ExprParser.Assert_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#import_stmt}.
	 * @param ctx the parse tree
	 */
	void enterImport_stmt(ExprParser.Import_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#import_stmt}.
	 * @param ctx the parse tree
	 */
	void exitImport_stmt(ExprParser.Import_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#import_name}.
	 * @param ctx the parse tree
	 */
	void enterImport_name(ExprParser.Import_nameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#import_name}.
	 * @param ctx the parse tree
	 */
	void exitImport_name(ExprParser.Import_nameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#import_from}.
	 * @param ctx the parse tree
	 */
	void enterImport_from(ExprParser.Import_fromContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#import_from}.
	 * @param ctx the parse tree
	 */
	void exitImport_from(ExprParser.Import_fromContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#import_from_targets}.
	 * @param ctx the parse tree
	 */
	void enterImport_from_targets(ExprParser.Import_from_targetsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#import_from_targets}.
	 * @param ctx the parse tree
	 */
	void exitImport_from_targets(ExprParser.Import_from_targetsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#import_from_as_names}.
	 * @param ctx the parse tree
	 */
	void enterImport_from_as_names(ExprParser.Import_from_as_namesContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#import_from_as_names}.
	 * @param ctx the parse tree
	 */
	void exitImport_from_as_names(ExprParser.Import_from_as_namesContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#import_from_as_name}.
	 * @param ctx the parse tree
	 */
	void enterImport_from_as_name(ExprParser.Import_from_as_nameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#import_from_as_name}.
	 * @param ctx the parse tree
	 */
	void exitImport_from_as_name(ExprParser.Import_from_as_nameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#dotted_as_names}.
	 * @param ctx the parse tree
	 */
	void enterDotted_as_names(ExprParser.Dotted_as_namesContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#dotted_as_names}.
	 * @param ctx the parse tree
	 */
	void exitDotted_as_names(ExprParser.Dotted_as_namesContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#dotted_as_name}.
	 * @param ctx the parse tree
	 */
	void enterDotted_as_name(ExprParser.Dotted_as_nameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#dotted_as_name}.
	 * @param ctx the parse tree
	 */
	void exitDotted_as_name(ExprParser.Dotted_as_nameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#dotted_name}.
	 * @param ctx the parse tree
	 */
	void enterDotted_name(ExprParser.Dotted_nameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#dotted_name}.
	 * @param ctx the parse tree
	 */
	void exitDotted_name(ExprParser.Dotted_nameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(ExprParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(ExprParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#decorators}.
	 * @param ctx the parse tree
	 */
	void enterDecorators(ExprParser.DecoratorsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#decorators}.
	 * @param ctx the parse tree
	 */
	void exitDecorators(ExprParser.DecoratorsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#class_def}.
	 * @param ctx the parse tree
	 */
	void enterClass_def(ExprParser.Class_defContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#class_def}.
	 * @param ctx the parse tree
	 */
	void exitClass_def(ExprParser.Class_defContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#class_def_raw}.
	 * @param ctx the parse tree
	 */
	void enterClass_def_raw(ExprParser.Class_def_rawContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#class_def_raw}.
	 * @param ctx the parse tree
	 */
	void exitClass_def_raw(ExprParser.Class_def_rawContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#function_def}.
	 * @param ctx the parse tree
	 */
	void enterFunction_def(ExprParser.Function_defContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#function_def}.
	 * @param ctx the parse tree
	 */
	void exitFunction_def(ExprParser.Function_defContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#function_def_raw}.
	 * @param ctx the parse tree
	 */
	void enterFunction_def_raw(ExprParser.Function_def_rawContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#function_def_raw}.
	 * @param ctx the parse tree
	 */
	void exitFunction_def_raw(ExprParser.Function_def_rawContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#params}.
	 * @param ctx the parse tree
	 */
	void enterParams(ExprParser.ParamsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#params}.
	 * @param ctx the parse tree
	 */
	void exitParams(ExprParser.ParamsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#parameters}.
	 * @param ctx the parse tree
	 */
	void enterParameters(ExprParser.ParametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#parameters}.
	 * @param ctx the parse tree
	 */
	void exitParameters(ExprParser.ParametersContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#slash_no_default}.
	 * @param ctx the parse tree
	 */
	void enterSlash_no_default(ExprParser.Slash_no_defaultContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#slash_no_default}.
	 * @param ctx the parse tree
	 */
	void exitSlash_no_default(ExprParser.Slash_no_defaultContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#slash_with_default}.
	 * @param ctx the parse tree
	 */
	void enterSlash_with_default(ExprParser.Slash_with_defaultContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#slash_with_default}.
	 * @param ctx the parse tree
	 */
	void exitSlash_with_default(ExprParser.Slash_with_defaultContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#star_etc}.
	 * @param ctx the parse tree
	 */
	void enterStar_etc(ExprParser.Star_etcContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#star_etc}.
	 * @param ctx the parse tree
	 */
	void exitStar_etc(ExprParser.Star_etcContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#kwds}.
	 * @param ctx the parse tree
	 */
	void enterKwds(ExprParser.KwdsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#kwds}.
	 * @param ctx the parse tree
	 */
	void exitKwds(ExprParser.KwdsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#param_no_default}.
	 * @param ctx the parse tree
	 */
	void enterParam_no_default(ExprParser.Param_no_defaultContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#param_no_default}.
	 * @param ctx the parse tree
	 */
	void exitParam_no_default(ExprParser.Param_no_defaultContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#param_no_default_star_annotation}.
	 * @param ctx the parse tree
	 */
	void enterParam_no_default_star_annotation(ExprParser.Param_no_default_star_annotationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#param_no_default_star_annotation}.
	 * @param ctx the parse tree
	 */
	void exitParam_no_default_star_annotation(ExprParser.Param_no_default_star_annotationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#param_with_default}.
	 * @param ctx the parse tree
	 */
	void enterParam_with_default(ExprParser.Param_with_defaultContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#param_with_default}.
	 * @param ctx the parse tree
	 */
	void exitParam_with_default(ExprParser.Param_with_defaultContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#param_maybe_default}.
	 * @param ctx the parse tree
	 */
	void enterParam_maybe_default(ExprParser.Param_maybe_defaultContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#param_maybe_default}.
	 * @param ctx the parse tree
	 */
	void exitParam_maybe_default(ExprParser.Param_maybe_defaultContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#param}.
	 * @param ctx the parse tree
	 */
	void enterParam(ExprParser.ParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#param}.
	 * @param ctx the parse tree
	 */
	void exitParam(ExprParser.ParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#param_star_annotation}.
	 * @param ctx the parse tree
	 */
	void enterParam_star_annotation(ExprParser.Param_star_annotationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#param_star_annotation}.
	 * @param ctx the parse tree
	 */
	void exitParam_star_annotation(ExprParser.Param_star_annotationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#annotation}.
	 * @param ctx the parse tree
	 */
	void enterAnnotation(ExprParser.AnnotationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#annotation}.
	 * @param ctx the parse tree
	 */
	void exitAnnotation(ExprParser.AnnotationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#star_annotation}.
	 * @param ctx the parse tree
	 */
	void enterStar_annotation(ExprParser.Star_annotationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#star_annotation}.
	 * @param ctx the parse tree
	 */
	void exitStar_annotation(ExprParser.Star_annotationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#default}.
	 * @param ctx the parse tree
	 */
	void enterDefault(ExprParser.DefaultContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#default}.
	 * @param ctx the parse tree
	 */
	void exitDefault(ExprParser.DefaultContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#if_stmt}.
	 * @param ctx the parse tree
	 */
	void enterIf_stmt(ExprParser.If_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#if_stmt}.
	 * @param ctx the parse tree
	 */
	void exitIf_stmt(ExprParser.If_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#elif_stmt}.
	 * @param ctx the parse tree
	 */
	void enterElif_stmt(ExprParser.Elif_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#elif_stmt}.
	 * @param ctx the parse tree
	 */
	void exitElif_stmt(ExprParser.Elif_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#else_block}.
	 * @param ctx the parse tree
	 */
	void enterElse_block(ExprParser.Else_blockContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#else_block}.
	 * @param ctx the parse tree
	 */
	void exitElse_block(ExprParser.Else_blockContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#while_stmt}.
	 * @param ctx the parse tree
	 */
	void enterWhile_stmt(ExprParser.While_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#while_stmt}.
	 * @param ctx the parse tree
	 */
	void exitWhile_stmt(ExprParser.While_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#for_stmt}.
	 * @param ctx the parse tree
	 */
	void enterFor_stmt(ExprParser.For_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#for_stmt}.
	 * @param ctx the parse tree
	 */
	void exitFor_stmt(ExprParser.For_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#with_stmt}.
	 * @param ctx the parse tree
	 */
	void enterWith_stmt(ExprParser.With_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#with_stmt}.
	 * @param ctx the parse tree
	 */
	void exitWith_stmt(ExprParser.With_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#with_item}.
	 * @param ctx the parse tree
	 */
	void enterWith_item(ExprParser.With_itemContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#with_item}.
	 * @param ctx the parse tree
	 */
	void exitWith_item(ExprParser.With_itemContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#try_stmt}.
	 * @param ctx the parse tree
	 */
	void enterTry_stmt(ExprParser.Try_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#try_stmt}.
	 * @param ctx the parse tree
	 */
	void exitTry_stmt(ExprParser.Try_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#except_block}.
	 * @param ctx the parse tree
	 */
	void enterExcept_block(ExprParser.Except_blockContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#except_block}.
	 * @param ctx the parse tree
	 */
	void exitExcept_block(ExprParser.Except_blockContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#except_star_block}.
	 * @param ctx the parse tree
	 */
	void enterExcept_star_block(ExprParser.Except_star_blockContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#except_star_block}.
	 * @param ctx the parse tree
	 */
	void exitExcept_star_block(ExprParser.Except_star_blockContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#finally_block}.
	 * @param ctx the parse tree
	 */
	void enterFinally_block(ExprParser.Finally_blockContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#finally_block}.
	 * @param ctx the parse tree
	 */
	void exitFinally_block(ExprParser.Finally_blockContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#match_stmt}.
	 * @param ctx the parse tree
	 */
	void enterMatch_stmt(ExprParser.Match_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#match_stmt}.
	 * @param ctx the parse tree
	 */
	void exitMatch_stmt(ExprParser.Match_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#subject_expr}.
	 * @param ctx the parse tree
	 */
	void enterSubject_expr(ExprParser.Subject_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#subject_expr}.
	 * @param ctx the parse tree
	 */
	void exitSubject_expr(ExprParser.Subject_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#case_block}.
	 * @param ctx the parse tree
	 */
	void enterCase_block(ExprParser.Case_blockContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#case_block}.
	 * @param ctx the parse tree
	 */
	void exitCase_block(ExprParser.Case_blockContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#guard}.
	 * @param ctx the parse tree
	 */
	void enterGuard(ExprParser.GuardContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#guard}.
	 * @param ctx the parse tree
	 */
	void exitGuard(ExprParser.GuardContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#patterns}.
	 * @param ctx the parse tree
	 */
	void enterPatterns(ExprParser.PatternsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#patterns}.
	 * @param ctx the parse tree
	 */
	void exitPatterns(ExprParser.PatternsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#pattern}.
	 * @param ctx the parse tree
	 */
	void enterPattern(ExprParser.PatternContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#pattern}.
	 * @param ctx the parse tree
	 */
	void exitPattern(ExprParser.PatternContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#as_pattern}.
	 * @param ctx the parse tree
	 */
	void enterAs_pattern(ExprParser.As_patternContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#as_pattern}.
	 * @param ctx the parse tree
	 */
	void exitAs_pattern(ExprParser.As_patternContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#or_pattern}.
	 * @param ctx the parse tree
	 */
	void enterOr_pattern(ExprParser.Or_patternContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#or_pattern}.
	 * @param ctx the parse tree
	 */
	void exitOr_pattern(ExprParser.Or_patternContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#closed_pattern}.
	 * @param ctx the parse tree
	 */
	void enterClosed_pattern(ExprParser.Closed_patternContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#closed_pattern}.
	 * @param ctx the parse tree
	 */
	void exitClosed_pattern(ExprParser.Closed_patternContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#literal_pattern}.
	 * @param ctx the parse tree
	 */
	void enterLiteral_pattern(ExprParser.Literal_patternContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#literal_pattern}.
	 * @param ctx the parse tree
	 */
	void exitLiteral_pattern(ExprParser.Literal_patternContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#literal_expr}.
	 * @param ctx the parse tree
	 */
	void enterLiteral_expr(ExprParser.Literal_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#literal_expr}.
	 * @param ctx the parse tree
	 */
	void exitLiteral_expr(ExprParser.Literal_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#complex_number}.
	 * @param ctx the parse tree
	 */
	void enterComplex_number(ExprParser.Complex_numberContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#complex_number}.
	 * @param ctx the parse tree
	 */
	void exitComplex_number(ExprParser.Complex_numberContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#signed_number}.
	 * @param ctx the parse tree
	 */
	void enterSigned_number(ExprParser.Signed_numberContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#signed_number}.
	 * @param ctx the parse tree
	 */
	void exitSigned_number(ExprParser.Signed_numberContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#signed_real_number}.
	 * @param ctx the parse tree
	 */
	void enterSigned_real_number(ExprParser.Signed_real_numberContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#signed_real_number}.
	 * @param ctx the parse tree
	 */
	void exitSigned_real_number(ExprParser.Signed_real_numberContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#real_number}.
	 * @param ctx the parse tree
	 */
	void enterReal_number(ExprParser.Real_numberContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#real_number}.
	 * @param ctx the parse tree
	 */
	void exitReal_number(ExprParser.Real_numberContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#imaginary_number}.
	 * @param ctx the parse tree
	 */
	void enterImaginary_number(ExprParser.Imaginary_numberContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#imaginary_number}.
	 * @param ctx the parse tree
	 */
	void exitImaginary_number(ExprParser.Imaginary_numberContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#capture_pattern}.
	 * @param ctx the parse tree
	 */
	void enterCapture_pattern(ExprParser.Capture_patternContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#capture_pattern}.
	 * @param ctx the parse tree
	 */
	void exitCapture_pattern(ExprParser.Capture_patternContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#pattern_capture_target}.
	 * @param ctx the parse tree
	 */
	void enterPattern_capture_target(ExprParser.Pattern_capture_targetContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#pattern_capture_target}.
	 * @param ctx the parse tree
	 */
	void exitPattern_capture_target(ExprParser.Pattern_capture_targetContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#wildcard_pattern}.
	 * @param ctx the parse tree
	 */
	void enterWildcard_pattern(ExprParser.Wildcard_patternContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#wildcard_pattern}.
	 * @param ctx the parse tree
	 */
	void exitWildcard_pattern(ExprParser.Wildcard_patternContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#value_pattern}.
	 * @param ctx the parse tree
	 */
	void enterValue_pattern(ExprParser.Value_patternContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#value_pattern}.
	 * @param ctx the parse tree
	 */
	void exitValue_pattern(ExprParser.Value_patternContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#attr}.
	 * @param ctx the parse tree
	 */
	void enterAttr(ExprParser.AttrContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#attr}.
	 * @param ctx the parse tree
	 */
	void exitAttr(ExprParser.AttrContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#name_or_attr}.
	 * @param ctx the parse tree
	 */
	void enterName_or_attr(ExprParser.Name_or_attrContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#name_or_attr}.
	 * @param ctx the parse tree
	 */
	void exitName_or_attr(ExprParser.Name_or_attrContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#group_pattern}.
	 * @param ctx the parse tree
	 */
	void enterGroup_pattern(ExprParser.Group_patternContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#group_pattern}.
	 * @param ctx the parse tree
	 */
	void exitGroup_pattern(ExprParser.Group_patternContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#sequence_pattern}.
	 * @param ctx the parse tree
	 */
	void enterSequence_pattern(ExprParser.Sequence_patternContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#sequence_pattern}.
	 * @param ctx the parse tree
	 */
	void exitSequence_pattern(ExprParser.Sequence_patternContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#open_sequence_pattern}.
	 * @param ctx the parse tree
	 */
	void enterOpen_sequence_pattern(ExprParser.Open_sequence_patternContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#open_sequence_pattern}.
	 * @param ctx the parse tree
	 */
	void exitOpen_sequence_pattern(ExprParser.Open_sequence_patternContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#maybe_sequence_pattern}.
	 * @param ctx the parse tree
	 */
	void enterMaybe_sequence_pattern(ExprParser.Maybe_sequence_patternContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#maybe_sequence_pattern}.
	 * @param ctx the parse tree
	 */
	void exitMaybe_sequence_pattern(ExprParser.Maybe_sequence_patternContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#maybe_star_pattern}.
	 * @param ctx the parse tree
	 */
	void enterMaybe_star_pattern(ExprParser.Maybe_star_patternContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#maybe_star_pattern}.
	 * @param ctx the parse tree
	 */
	void exitMaybe_star_pattern(ExprParser.Maybe_star_patternContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#star_pattern}.
	 * @param ctx the parse tree
	 */
	void enterStar_pattern(ExprParser.Star_patternContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#star_pattern}.
	 * @param ctx the parse tree
	 */
	void exitStar_pattern(ExprParser.Star_patternContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#mapping_pattern}.
	 * @param ctx the parse tree
	 */
	void enterMapping_pattern(ExprParser.Mapping_patternContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#mapping_pattern}.
	 * @param ctx the parse tree
	 */
	void exitMapping_pattern(ExprParser.Mapping_patternContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#items_pattern}.
	 * @param ctx the parse tree
	 */
	void enterItems_pattern(ExprParser.Items_patternContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#items_pattern}.
	 * @param ctx the parse tree
	 */
	void exitItems_pattern(ExprParser.Items_patternContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#key_value_pattern}.
	 * @param ctx the parse tree
	 */
	void enterKey_value_pattern(ExprParser.Key_value_patternContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#key_value_pattern}.
	 * @param ctx the parse tree
	 */
	void exitKey_value_pattern(ExprParser.Key_value_patternContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#double_star_pattern}.
	 * @param ctx the parse tree
	 */
	void enterDouble_star_pattern(ExprParser.Double_star_patternContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#double_star_pattern}.
	 * @param ctx the parse tree
	 */
	void exitDouble_star_pattern(ExprParser.Double_star_patternContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#class_pattern}.
	 * @param ctx the parse tree
	 */
	void enterClass_pattern(ExprParser.Class_patternContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#class_pattern}.
	 * @param ctx the parse tree
	 */
	void exitClass_pattern(ExprParser.Class_patternContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#positional_patterns}.
	 * @param ctx the parse tree
	 */
	void enterPositional_patterns(ExprParser.Positional_patternsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#positional_patterns}.
	 * @param ctx the parse tree
	 */
	void exitPositional_patterns(ExprParser.Positional_patternsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#keyword_patterns}.
	 * @param ctx the parse tree
	 */
	void enterKeyword_patterns(ExprParser.Keyword_patternsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#keyword_patterns}.
	 * @param ctx the parse tree
	 */
	void exitKeyword_patterns(ExprParser.Keyword_patternsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#keyword_pattern}.
	 * @param ctx the parse tree
	 */
	void enterKeyword_pattern(ExprParser.Keyword_patternContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#keyword_pattern}.
	 * @param ctx the parse tree
	 */
	void exitKeyword_pattern(ExprParser.Keyword_patternContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#type_alias}.
	 * @param ctx the parse tree
	 */
	void enterType_alias(ExprParser.Type_aliasContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#type_alias}.
	 * @param ctx the parse tree
	 */
	void exitType_alias(ExprParser.Type_aliasContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#type_params}.
	 * @param ctx the parse tree
	 */
	void enterType_params(ExprParser.Type_paramsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#type_params}.
	 * @param ctx the parse tree
	 */
	void exitType_params(ExprParser.Type_paramsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#type_param_seq}.
	 * @param ctx the parse tree
	 */
	void enterType_param_seq(ExprParser.Type_param_seqContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#type_param_seq}.
	 * @param ctx the parse tree
	 */
	void exitType_param_seq(ExprParser.Type_param_seqContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#type_param}.
	 * @param ctx the parse tree
	 */
	void enterType_param(ExprParser.Type_paramContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#type_param}.
	 * @param ctx the parse tree
	 */
	void exitType_param(ExprParser.Type_paramContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#type_param_bound}.
	 * @param ctx the parse tree
	 */
	void enterType_param_bound(ExprParser.Type_param_boundContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#type_param_bound}.
	 * @param ctx the parse tree
	 */
	void exitType_param_bound(ExprParser.Type_param_boundContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#type_param_default}.
	 * @param ctx the parse tree
	 */
	void enterType_param_default(ExprParser.Type_param_defaultContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#type_param_default}.
	 * @param ctx the parse tree
	 */
	void exitType_param_default(ExprParser.Type_param_defaultContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#type_param_starred_default}.
	 * @param ctx the parse tree
	 */
	void enterType_param_starred_default(ExprParser.Type_param_starred_defaultContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#type_param_starred_default}.
	 * @param ctx the parse tree
	 */
	void exitType_param_starred_default(ExprParser.Type_param_starred_defaultContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#expressions}.
	 * @param ctx the parse tree
	 */
	void enterExpressions(ExprParser.ExpressionsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#expressions}.
	 * @param ctx the parse tree
	 */
	void exitExpressions(ExprParser.ExpressionsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(ExprParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(ExprParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#yield_expr}.
	 * @param ctx the parse tree
	 */
	void enterYield_expr(ExprParser.Yield_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#yield_expr}.
	 * @param ctx the parse tree
	 */
	void exitYield_expr(ExprParser.Yield_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#star_expressions}.
	 * @param ctx the parse tree
	 */
	void enterStar_expressions(ExprParser.Star_expressionsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#star_expressions}.
	 * @param ctx the parse tree
	 */
	void exitStar_expressions(ExprParser.Star_expressionsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#star_expression}.
	 * @param ctx the parse tree
	 */
	void enterStar_expression(ExprParser.Star_expressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#star_expression}.
	 * @param ctx the parse tree
	 */
	void exitStar_expression(ExprParser.Star_expressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#star_named_expressions}.
	 * @param ctx the parse tree
	 */
	void enterStar_named_expressions(ExprParser.Star_named_expressionsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#star_named_expressions}.
	 * @param ctx the parse tree
	 */
	void exitStar_named_expressions(ExprParser.Star_named_expressionsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#star_named_expression}.
	 * @param ctx the parse tree
	 */
	void enterStar_named_expression(ExprParser.Star_named_expressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#star_named_expression}.
	 * @param ctx the parse tree
	 */
	void exitStar_named_expression(ExprParser.Star_named_expressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#assignment_expression}.
	 * @param ctx the parse tree
	 */
	void enterAssignment_expression(ExprParser.Assignment_expressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#assignment_expression}.
	 * @param ctx the parse tree
	 */
	void exitAssignment_expression(ExprParser.Assignment_expressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#named_expression}.
	 * @param ctx the parse tree
	 */
	void enterNamed_expression(ExprParser.Named_expressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#named_expression}.
	 * @param ctx the parse tree
	 */
	void exitNamed_expression(ExprParser.Named_expressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#disjunction}.
	 * @param ctx the parse tree
	 */
	void enterDisjunction(ExprParser.DisjunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#disjunction}.
	 * @param ctx the parse tree
	 */
	void exitDisjunction(ExprParser.DisjunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#conjunction}.
	 * @param ctx the parse tree
	 */
	void enterConjunction(ExprParser.ConjunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#conjunction}.
	 * @param ctx the parse tree
	 */
	void exitConjunction(ExprParser.ConjunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#inversion}.
	 * @param ctx the parse tree
	 */
	void enterInversion(ExprParser.InversionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#inversion}.
	 * @param ctx the parse tree
	 */
	void exitInversion(ExprParser.InversionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#comparison}.
	 * @param ctx the parse tree
	 */
	void enterComparison(ExprParser.ComparisonContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#comparison}.
	 * @param ctx the parse tree
	 */
	void exitComparison(ExprParser.ComparisonContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#compare_op_bitwise_or_pair}.
	 * @param ctx the parse tree
	 */
	void enterCompare_op_bitwise_or_pair(ExprParser.Compare_op_bitwise_or_pairContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#compare_op_bitwise_or_pair}.
	 * @param ctx the parse tree
	 */
	void exitCompare_op_bitwise_or_pair(ExprParser.Compare_op_bitwise_or_pairContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#eq_bitwise_or}.
	 * @param ctx the parse tree
	 */
	void enterEq_bitwise_or(ExprParser.Eq_bitwise_orContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#eq_bitwise_or}.
	 * @param ctx the parse tree
	 */
	void exitEq_bitwise_or(ExprParser.Eq_bitwise_orContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#noteq_bitwise_or}.
	 * @param ctx the parse tree
	 */
	void enterNoteq_bitwise_or(ExprParser.Noteq_bitwise_orContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#noteq_bitwise_or}.
	 * @param ctx the parse tree
	 */
	void exitNoteq_bitwise_or(ExprParser.Noteq_bitwise_orContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#lte_bitwise_or}.
	 * @param ctx the parse tree
	 */
	void enterLte_bitwise_or(ExprParser.Lte_bitwise_orContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#lte_bitwise_or}.
	 * @param ctx the parse tree
	 */
	void exitLte_bitwise_or(ExprParser.Lte_bitwise_orContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#lt_bitwise_or}.
	 * @param ctx the parse tree
	 */
	void enterLt_bitwise_or(ExprParser.Lt_bitwise_orContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#lt_bitwise_or}.
	 * @param ctx the parse tree
	 */
	void exitLt_bitwise_or(ExprParser.Lt_bitwise_orContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#gte_bitwise_or}.
	 * @param ctx the parse tree
	 */
	void enterGte_bitwise_or(ExprParser.Gte_bitwise_orContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#gte_bitwise_or}.
	 * @param ctx the parse tree
	 */
	void exitGte_bitwise_or(ExprParser.Gte_bitwise_orContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#gt_bitwise_or}.
	 * @param ctx the parse tree
	 */
	void enterGt_bitwise_or(ExprParser.Gt_bitwise_orContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#gt_bitwise_or}.
	 * @param ctx the parse tree
	 */
	void exitGt_bitwise_or(ExprParser.Gt_bitwise_orContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#notin_bitwise_or}.
	 * @param ctx the parse tree
	 */
	void enterNotin_bitwise_or(ExprParser.Notin_bitwise_orContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#notin_bitwise_or}.
	 * @param ctx the parse tree
	 */
	void exitNotin_bitwise_or(ExprParser.Notin_bitwise_orContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#in_bitwise_or}.
	 * @param ctx the parse tree
	 */
	void enterIn_bitwise_or(ExprParser.In_bitwise_orContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#in_bitwise_or}.
	 * @param ctx the parse tree
	 */
	void exitIn_bitwise_or(ExprParser.In_bitwise_orContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#isnot_bitwise_or}.
	 * @param ctx the parse tree
	 */
	void enterIsnot_bitwise_or(ExprParser.Isnot_bitwise_orContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#isnot_bitwise_or}.
	 * @param ctx the parse tree
	 */
	void exitIsnot_bitwise_or(ExprParser.Isnot_bitwise_orContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#is_bitwise_or}.
	 * @param ctx the parse tree
	 */
	void enterIs_bitwise_or(ExprParser.Is_bitwise_orContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#is_bitwise_or}.
	 * @param ctx the parse tree
	 */
	void exitIs_bitwise_or(ExprParser.Is_bitwise_orContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#bitwise_or}.
	 * @param ctx the parse tree
	 */
	void enterBitwise_or(ExprParser.Bitwise_orContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#bitwise_or}.
	 * @param ctx the parse tree
	 */
	void exitBitwise_or(ExprParser.Bitwise_orContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#bitwise_xor}.
	 * @param ctx the parse tree
	 */
	void enterBitwise_xor(ExprParser.Bitwise_xorContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#bitwise_xor}.
	 * @param ctx the parse tree
	 */
	void exitBitwise_xor(ExprParser.Bitwise_xorContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#bitwise_and}.
	 * @param ctx the parse tree
	 */
	void enterBitwise_and(ExprParser.Bitwise_andContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#bitwise_and}.
	 * @param ctx the parse tree
	 */
	void exitBitwise_and(ExprParser.Bitwise_andContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#shift_expr}.
	 * @param ctx the parse tree
	 */
	void enterShift_expr(ExprParser.Shift_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#shift_expr}.
	 * @param ctx the parse tree
	 */
	void exitShift_expr(ExprParser.Shift_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#sum}.
	 * @param ctx the parse tree
	 */
	void enterSum(ExprParser.SumContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#sum}.
	 * @param ctx the parse tree
	 */
	void exitSum(ExprParser.SumContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(ExprParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(ExprParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(ExprParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(ExprParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#power}.
	 * @param ctx the parse tree
	 */
	void enterPower(ExprParser.PowerContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#power}.
	 * @param ctx the parse tree
	 */
	void exitPower(ExprParser.PowerContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#await_primary}.
	 * @param ctx the parse tree
	 */
	void enterAwait_primary(ExprParser.Await_primaryContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#await_primary}.
	 * @param ctx the parse tree
	 */
	void exitAwait_primary(ExprParser.Await_primaryContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#primary}.
	 * @param ctx the parse tree
	 */
	void enterPrimary(ExprParser.PrimaryContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#primary}.
	 * @param ctx the parse tree
	 */
	void exitPrimary(ExprParser.PrimaryContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#slices}.
	 * @param ctx the parse tree
	 */
	void enterSlices(ExprParser.SlicesContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#slices}.
	 * @param ctx the parse tree
	 */
	void exitSlices(ExprParser.SlicesContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#slice}.
	 * @param ctx the parse tree
	 */
	void enterSlice(ExprParser.SliceContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#slice}.
	 * @param ctx the parse tree
	 */
	void exitSlice(ExprParser.SliceContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterAtom(ExprParser.AtomContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitAtom(ExprParser.AtomContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#group}.
	 * @param ctx the parse tree
	 */
	void enterGroup(ExprParser.GroupContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#group}.
	 * @param ctx the parse tree
	 */
	void exitGroup(ExprParser.GroupContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#lambdef}.
	 * @param ctx the parse tree
	 */
	void enterLambdef(ExprParser.LambdefContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#lambdef}.
	 * @param ctx the parse tree
	 */
	void exitLambdef(ExprParser.LambdefContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#lambda_params}.
	 * @param ctx the parse tree
	 */
	void enterLambda_params(ExprParser.Lambda_paramsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#lambda_params}.
	 * @param ctx the parse tree
	 */
	void exitLambda_params(ExprParser.Lambda_paramsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#lambda_parameters}.
	 * @param ctx the parse tree
	 */
	void enterLambda_parameters(ExprParser.Lambda_parametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#lambda_parameters}.
	 * @param ctx the parse tree
	 */
	void exitLambda_parameters(ExprParser.Lambda_parametersContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#lambda_slash_no_default}.
	 * @param ctx the parse tree
	 */
	void enterLambda_slash_no_default(ExprParser.Lambda_slash_no_defaultContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#lambda_slash_no_default}.
	 * @param ctx the parse tree
	 */
	void exitLambda_slash_no_default(ExprParser.Lambda_slash_no_defaultContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#lambda_slash_with_default}.
	 * @param ctx the parse tree
	 */
	void enterLambda_slash_with_default(ExprParser.Lambda_slash_with_defaultContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#lambda_slash_with_default}.
	 * @param ctx the parse tree
	 */
	void exitLambda_slash_with_default(ExprParser.Lambda_slash_with_defaultContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#lambda_star_etc}.
	 * @param ctx the parse tree
	 */
	void enterLambda_star_etc(ExprParser.Lambda_star_etcContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#lambda_star_etc}.
	 * @param ctx the parse tree
	 */
	void exitLambda_star_etc(ExprParser.Lambda_star_etcContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#lambda_kwds}.
	 * @param ctx the parse tree
	 */
	void enterLambda_kwds(ExprParser.Lambda_kwdsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#lambda_kwds}.
	 * @param ctx the parse tree
	 */
	void exitLambda_kwds(ExprParser.Lambda_kwdsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#lambda_param_no_default}.
	 * @param ctx the parse tree
	 */
	void enterLambda_param_no_default(ExprParser.Lambda_param_no_defaultContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#lambda_param_no_default}.
	 * @param ctx the parse tree
	 */
	void exitLambda_param_no_default(ExprParser.Lambda_param_no_defaultContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#lambda_param_with_default}.
	 * @param ctx the parse tree
	 */
	void enterLambda_param_with_default(ExprParser.Lambda_param_with_defaultContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#lambda_param_with_default}.
	 * @param ctx the parse tree
	 */
	void exitLambda_param_with_default(ExprParser.Lambda_param_with_defaultContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#lambda_param_maybe_default}.
	 * @param ctx the parse tree
	 */
	void enterLambda_param_maybe_default(ExprParser.Lambda_param_maybe_defaultContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#lambda_param_maybe_default}.
	 * @param ctx the parse tree
	 */
	void exitLambda_param_maybe_default(ExprParser.Lambda_param_maybe_defaultContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#lambda_param}.
	 * @param ctx the parse tree
	 */
	void enterLambda_param(ExprParser.Lambda_paramContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#lambda_param}.
	 * @param ctx the parse tree
	 */
	void exitLambda_param(ExprParser.Lambda_paramContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#fstring_middle}.
	 * @param ctx the parse tree
	 */
	void enterFstring_middle(ExprParser.Fstring_middleContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#fstring_middle}.
	 * @param ctx the parse tree
	 */
	void exitFstring_middle(ExprParser.Fstring_middleContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#fstring_replacement_field}.
	 * @param ctx the parse tree
	 */
	void enterFstring_replacement_field(ExprParser.Fstring_replacement_fieldContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#fstring_replacement_field}.
	 * @param ctx the parse tree
	 */
	void exitFstring_replacement_field(ExprParser.Fstring_replacement_fieldContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#fstring_conversion}.
	 * @param ctx the parse tree
	 */
	void enterFstring_conversion(ExprParser.Fstring_conversionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#fstring_conversion}.
	 * @param ctx the parse tree
	 */
	void exitFstring_conversion(ExprParser.Fstring_conversionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#fstring_full_format_spec}.
	 * @param ctx the parse tree
	 */
	void enterFstring_full_format_spec(ExprParser.Fstring_full_format_specContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#fstring_full_format_spec}.
	 * @param ctx the parse tree
	 */
	void exitFstring_full_format_spec(ExprParser.Fstring_full_format_specContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#fstring_format_spec}.
	 * @param ctx the parse tree
	 */
	void enterFstring_format_spec(ExprParser.Fstring_format_specContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#fstring_format_spec}.
	 * @param ctx the parse tree
	 */
	void exitFstring_format_spec(ExprParser.Fstring_format_specContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#fstring}.
	 * @param ctx the parse tree
	 */
	void enterFstring(ExprParser.FstringContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#fstring}.
	 * @param ctx the parse tree
	 */
	void exitFstring(ExprParser.FstringContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#tstring_format_spec_replacement_field}.
	 * @param ctx the parse tree
	 */
	void enterTstring_format_spec_replacement_field(ExprParser.Tstring_format_spec_replacement_fieldContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#tstring_format_spec_replacement_field}.
	 * @param ctx the parse tree
	 */
	void exitTstring_format_spec_replacement_field(ExprParser.Tstring_format_spec_replacement_fieldContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#tstring_format_spec}.
	 * @param ctx the parse tree
	 */
	void enterTstring_format_spec(ExprParser.Tstring_format_specContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#tstring_format_spec}.
	 * @param ctx the parse tree
	 */
	void exitTstring_format_spec(ExprParser.Tstring_format_specContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#tstring_full_format_spec}.
	 * @param ctx the parse tree
	 */
	void enterTstring_full_format_spec(ExprParser.Tstring_full_format_specContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#tstring_full_format_spec}.
	 * @param ctx the parse tree
	 */
	void exitTstring_full_format_spec(ExprParser.Tstring_full_format_specContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#tstring_replacement_field}.
	 * @param ctx the parse tree
	 */
	void enterTstring_replacement_field(ExprParser.Tstring_replacement_fieldContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#tstring_replacement_field}.
	 * @param ctx the parse tree
	 */
	void exitTstring_replacement_field(ExprParser.Tstring_replacement_fieldContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#tstring_middle}.
	 * @param ctx the parse tree
	 */
	void enterTstring_middle(ExprParser.Tstring_middleContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#tstring_middle}.
	 * @param ctx the parse tree
	 */
	void exitTstring_middle(ExprParser.Tstring_middleContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#tstring}.
	 * @param ctx the parse tree
	 */
	void enterTstring(ExprParser.TstringContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#tstring}.
	 * @param ctx the parse tree
	 */
	void exitTstring(ExprParser.TstringContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#string}.
	 * @param ctx the parse tree
	 */
	void enterString(ExprParser.StringContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#string}.
	 * @param ctx the parse tree
	 */
	void exitString(ExprParser.StringContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#strings}.
	 * @param ctx the parse tree
	 */
	void enterStrings(ExprParser.StringsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#strings}.
	 * @param ctx the parse tree
	 */
	void exitStrings(ExprParser.StringsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#list}.
	 * @param ctx the parse tree
	 */
	void enterList(ExprParser.ListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#list}.
	 * @param ctx the parse tree
	 */
	void exitList(ExprParser.ListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#tuple}.
	 * @param ctx the parse tree
	 */
	void enterTuple(ExprParser.TupleContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#tuple}.
	 * @param ctx the parse tree
	 */
	void exitTuple(ExprParser.TupleContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#set}.
	 * @param ctx the parse tree
	 */
	void enterSet(ExprParser.SetContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#set}.
	 * @param ctx the parse tree
	 */
	void exitSet(ExprParser.SetContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#dict}.
	 * @param ctx the parse tree
	 */
	void enterDict(ExprParser.DictContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#dict}.
	 * @param ctx the parse tree
	 */
	void exitDict(ExprParser.DictContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#double_starred_kvpairs}.
	 * @param ctx the parse tree
	 */
	void enterDouble_starred_kvpairs(ExprParser.Double_starred_kvpairsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#double_starred_kvpairs}.
	 * @param ctx the parse tree
	 */
	void exitDouble_starred_kvpairs(ExprParser.Double_starred_kvpairsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#double_starred_kvpair}.
	 * @param ctx the parse tree
	 */
	void enterDouble_starred_kvpair(ExprParser.Double_starred_kvpairContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#double_starred_kvpair}.
	 * @param ctx the parse tree
	 */
	void exitDouble_starred_kvpair(ExprParser.Double_starred_kvpairContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#kvpair}.
	 * @param ctx the parse tree
	 */
	void enterKvpair(ExprParser.KvpairContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#kvpair}.
	 * @param ctx the parse tree
	 */
	void exitKvpair(ExprParser.KvpairContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#for_if_clauses}.
	 * @param ctx the parse tree
	 */
	void enterFor_if_clauses(ExprParser.For_if_clausesContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#for_if_clauses}.
	 * @param ctx the parse tree
	 */
	void exitFor_if_clauses(ExprParser.For_if_clausesContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#for_if_clause}.
	 * @param ctx the parse tree
	 */
	void enterFor_if_clause(ExprParser.For_if_clauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#for_if_clause}.
	 * @param ctx the parse tree
	 */
	void exitFor_if_clause(ExprParser.For_if_clauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#listcomp}.
	 * @param ctx the parse tree
	 */
	void enterListcomp(ExprParser.ListcompContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#listcomp}.
	 * @param ctx the parse tree
	 */
	void exitListcomp(ExprParser.ListcompContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#setcomp}.
	 * @param ctx the parse tree
	 */
	void enterSetcomp(ExprParser.SetcompContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#setcomp}.
	 * @param ctx the parse tree
	 */
	void exitSetcomp(ExprParser.SetcompContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#genexp}.
	 * @param ctx the parse tree
	 */
	void enterGenexp(ExprParser.GenexpContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#genexp}.
	 * @param ctx the parse tree
	 */
	void exitGenexp(ExprParser.GenexpContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#dictcomp}.
	 * @param ctx the parse tree
	 */
	void enterDictcomp(ExprParser.DictcompContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#dictcomp}.
	 * @param ctx the parse tree
	 */
	void exitDictcomp(ExprParser.DictcompContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#arguments}.
	 * @param ctx the parse tree
	 */
	void enterArguments(ExprParser.ArgumentsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#arguments}.
	 * @param ctx the parse tree
	 */
	void exitArguments(ExprParser.ArgumentsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#args}.
	 * @param ctx the parse tree
	 */
	void enterArgs(ExprParser.ArgsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#args}.
	 * @param ctx the parse tree
	 */
	void exitArgs(ExprParser.ArgsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#kwargs}.
	 * @param ctx the parse tree
	 */
	void enterKwargs(ExprParser.KwargsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#kwargs}.
	 * @param ctx the parse tree
	 */
	void exitKwargs(ExprParser.KwargsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#starred_expression}.
	 * @param ctx the parse tree
	 */
	void enterStarred_expression(ExprParser.Starred_expressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#starred_expression}.
	 * @param ctx the parse tree
	 */
	void exitStarred_expression(ExprParser.Starred_expressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#kwarg_or_starred}.
	 * @param ctx the parse tree
	 */
	void enterKwarg_or_starred(ExprParser.Kwarg_or_starredContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#kwarg_or_starred}.
	 * @param ctx the parse tree
	 */
	void exitKwarg_or_starred(ExprParser.Kwarg_or_starredContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#kwarg_or_double_starred}.
	 * @param ctx the parse tree
	 */
	void enterKwarg_or_double_starred(ExprParser.Kwarg_or_double_starredContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#kwarg_or_double_starred}.
	 * @param ctx the parse tree
	 */
	void exitKwarg_or_double_starred(ExprParser.Kwarg_or_double_starredContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#star_targets}.
	 * @param ctx the parse tree
	 */
	void enterStar_targets(ExprParser.Star_targetsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#star_targets}.
	 * @param ctx the parse tree
	 */
	void exitStar_targets(ExprParser.Star_targetsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#star_targets_list_seq}.
	 * @param ctx the parse tree
	 */
	void enterStar_targets_list_seq(ExprParser.Star_targets_list_seqContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#star_targets_list_seq}.
	 * @param ctx the parse tree
	 */
	void exitStar_targets_list_seq(ExprParser.Star_targets_list_seqContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#star_targets_tuple_seq}.
	 * @param ctx the parse tree
	 */
	void enterStar_targets_tuple_seq(ExprParser.Star_targets_tuple_seqContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#star_targets_tuple_seq}.
	 * @param ctx the parse tree
	 */
	void exitStar_targets_tuple_seq(ExprParser.Star_targets_tuple_seqContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#star_target}.
	 * @param ctx the parse tree
	 */
	void enterStar_target(ExprParser.Star_targetContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#star_target}.
	 * @param ctx the parse tree
	 */
	void exitStar_target(ExprParser.Star_targetContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#target_with_star_atom}.
	 * @param ctx the parse tree
	 */
	void enterTarget_with_star_atom(ExprParser.Target_with_star_atomContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#target_with_star_atom}.
	 * @param ctx the parse tree
	 */
	void exitTarget_with_star_atom(ExprParser.Target_with_star_atomContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#star_atom}.
	 * @param ctx the parse tree
	 */
	void enterStar_atom(ExprParser.Star_atomContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#star_atom}.
	 * @param ctx the parse tree
	 */
	void exitStar_atom(ExprParser.Star_atomContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#single_target}.
	 * @param ctx the parse tree
	 */
	void enterSingle_target(ExprParser.Single_targetContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#single_target}.
	 * @param ctx the parse tree
	 */
	void exitSingle_target(ExprParser.Single_targetContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#single_subscript_attribute_target}.
	 * @param ctx the parse tree
	 */
	void enterSingle_subscript_attribute_target(ExprParser.Single_subscript_attribute_targetContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#single_subscript_attribute_target}.
	 * @param ctx the parse tree
	 */
	void exitSingle_subscript_attribute_target(ExprParser.Single_subscript_attribute_targetContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#t_primary}.
	 * @param ctx the parse tree
	 */
	void enterT_primary(ExprParser.T_primaryContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#t_primary}.
	 * @param ctx the parse tree
	 */
	void exitT_primary(ExprParser.T_primaryContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#t_lookahead}.
	 * @param ctx the parse tree
	 */
	void enterT_lookahead(ExprParser.T_lookaheadContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#t_lookahead}.
	 * @param ctx the parse tree
	 */
	void exitT_lookahead(ExprParser.T_lookaheadContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#del_targets}.
	 * @param ctx the parse tree
	 */
	void enterDel_targets(ExprParser.Del_targetsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#del_targets}.
	 * @param ctx the parse tree
	 */
	void exitDel_targets(ExprParser.Del_targetsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#del_target}.
	 * @param ctx the parse tree
	 */
	void enterDel_target(ExprParser.Del_targetContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#del_target}.
	 * @param ctx the parse tree
	 */
	void exitDel_target(ExprParser.Del_targetContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#del_t_atom}.
	 * @param ctx the parse tree
	 */
	void enterDel_t_atom(ExprParser.Del_t_atomContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#del_t_atom}.
	 * @param ctx the parse tree
	 */
	void exitDel_t_atom(ExprParser.Del_t_atomContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#type_expressions}.
	 * @param ctx the parse tree
	 */
	void enterType_expressions(ExprParser.Type_expressionsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#type_expressions}.
	 * @param ctx the parse tree
	 */
	void exitType_expressions(ExprParser.Type_expressionsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#func_type_comment}.
	 * @param ctx the parse tree
	 */
	void enterFunc_type_comment(ExprParser.Func_type_commentContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#func_type_comment}.
	 * @param ctx the parse tree
	 */
	void exitFunc_type_comment(ExprParser.Func_type_commentContext ctx);
}